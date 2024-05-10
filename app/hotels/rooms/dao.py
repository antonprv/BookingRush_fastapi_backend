from datetime import date

from sqlalchemy import select, func, and_, or_

from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.bookings.models import Bookings
from app.database import async_session_maker


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(
            cls,
            hotel_id: int,
            date_from: date,
            date_to: date
    ):

        booked_rooms = select(
            Bookings.room_id,
            func.count(Bookings.room_id).label('total_booked_rooms')
        ).where(
            or_(
                and_(
                    (Bookings.date_from >= date_from),
                    (Bookings.date_from <= date_to)
                ),
                and_(
                    (Bookings.date_from <= date_from),
                    (Bookings.date_to <= date_from)
                )
            )
        ).group_by(Bookings.room_id).cte('booked_rooms')

        get_rooms = select(
            Rooms.__table__.columns,
            (Rooms.price * (date_to - date_from).days).label('total_cost'),
            (Rooms.quantity - func.coalesce(
                booked_rooms.c.total_booked_rooms, 0)).label('rooms_left'),
        ).join(
            booked_rooms,
            booked_rooms.c.room_id == Rooms.id,
            isouter=True
        ).where(Rooms.hotel_id == hotel_id)

        async with async_session_maker() as session:
            avaliable_hotels = await session.execute(get_rooms)
            return avaliable_hotels.mappings.all()
from collections import ChainMap
from datetime import date

from sqlalchemy import select, func, and_, or_

from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms
from app.hotels.models import Hotels


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all(
            cls,
            location: str,
            date_from: date,
            date_to: date
    ):
        # I've visually split  a single SQL-query into 3
        # docstrings for convenience.
        """
        WITH booked_rooms AS (
            SELECT room_id, COUNT(room_id) AS rooms_booked
                FROM bookings
                WHERE
                    (date_from >= '2023-05-15' AND
                    date_from <= '2023-06-20') OR
                    (date_from <= '2023-05-15' AND
                    date_to > '2023-05-15')
                GROUP BY room_id
            ),
        """
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

        # If all rooms are avaliable for a selected date,
        # booked_rooms returns a Null value, which could
        # potentially break the code. So I use the
        # COALESCE func to replace Null value with 0.
        """
        booked_hotels AS (
            SELECT hotel_id, SUM(rooms.quantity - COALESCE(rooms_booked, 0))
             AS rooms_left
            FROM rooms
            LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
            GROUP BY hotel_id
        )
        """
        booked_hotels = select(
            Rooms.hotel_id,
            func.sum(
                Rooms.quantity - func.coalesce(
                    booked_rooms.c.total_booked_rooms, 0
                )
            ).label('rooms_left')
        ).select_from(Rooms).join(
            booked_rooms,
            booked_rooms.c.room_id == Rooms.id,
            isouter=True
        ).group_by(Rooms.hotel_id).cte('booked_hotels')

        # I use Hotels.__table__.columns so that
        # SQLAlchemy would output everything as
        # a single dict, which is much easier to parse
        # for pydantic.
        """
        SELECT * FROM hotels
        LEFT JOIN booked_hotels ON booked_hotels.hotel_id = hotels.id
        WHERE rooms_left > 0 AND location LIKE '%Алтай%';
        """
        get_available_hotels = select(
            Hotels.__table__.columns,
            booked_hotels.c.rooms_left
        ).join(booked_hotels, booked_hotels.c.hotel_id == Hotels.id,
               isouter=True).where(
            and_(
                (booked_hotels.c.rooms_left > 0),
                Hotels.location.like(f'%{location}%')
            )
        )

        async with async_session_maker() as session:
            available_hotels = await session.execute(get_available_hotels)
            return available_hotels.mappings().all()

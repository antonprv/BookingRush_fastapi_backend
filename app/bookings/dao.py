# Ещё могут быть названия repo, service.
# DAO - Data Acess Object
from datetime import date

from pydantic import EmailStr
from sqlalchemy import select, insert, func, delete, and_, or_
from sqlalchemy.exc import SQLAlchemyError

from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms
from app.users.models import Users
from app.hotels.models import Hotels
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.exceptions import RoomFullyBookedException, \
    BookingsNotFoundException


class BookingsDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def find_all_for_user(
            cls,
            user_id: int
    ):
        try:
            get_bookings = select(
                Bookings.__table__.columns,
                Rooms.__table__.columns
            ).join(
                Rooms, Bookings.room_id == Rooms.id
            ).where(Bookings.user_id == user_id)

            async with async_session_maker() as session:
                user_bookings = await session.execute(get_bookings)

                if not user_bookings:
                    raise BookingsNotFoundException
                else:
                    return user_bookings.mappings().all()
        except BookingsNotFoundException:
            raise BookingsNotFoundException

    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        """
        WITH booked_rooms AS (
            SELECT * FROM bookings
            WHERE room_id = 1 AND
                (date_from >= '2023-05-15' AND date_from <= '2023-06-20')
                 OR
                (date_from <= '2023-05-15' AND date_to > '2023-05-15')
        )
        """

        try:
            async with async_session_maker() as session:
                booked_rooms = select(Bookings).where(
                    and_(
                        Bookings.room_id == room_id,
                        or_(
                            and_(
                                Bookings.date_from >= date_from,
                                Bookings.date_from <= date_to,
                            ),
                            and_(
                                Bookings.date_from <= date_from,
                                Bookings.date_to > date_from,
                            ),
                        ),
                    )
                ).cte("booked_rooms")

                """
                SELECT rooms.quantity - COUNT(booked_rooms.room_id)
                FROM rooms
                LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
                WHERE rooms.id = 1
                GROUP BY rooms.quantity, booked_rooms.room_id
                """

                get_rooms_left = select(
                    (Rooms.quantity -
                     func.coalesce(func.count(booked_rooms.c.room_id), 0)
                     ).label('rooms left')
                ).select_from(Rooms).join(
                    booked_rooms,
                    booked_rooms.c.room_id == Rooms.id,
                    isouter=True
                ).where(Rooms.id == room_id
                        ).group_by(
                    Rooms.quantity, booked_rooms.c.room_id
                )

                rooms_left = await session.execute(get_rooms_left)
                rooms_left: int = rooms_left.scalar()

                if rooms_left > 0:
                    get_price = select(Rooms.price).filter_by(id=room_id)
                    price = await session.execute(get_price)
                    price: int = price.scalar()
                    add_booking = (
                        insert(Bookings).values(
                            room_id=room_id,
                            user_id=user_id,
                            date_from=date_from,
                            date_to=date_to,
                            price=price,
                        ).returning(
                            Bookings.id,
                            Bookings.user_id,
                            Bookings.room_id,
                            Bookings.date_from,
                            Bookings.date_to,
                        )
                    )

                    new_booking = await session.execute(add_booking)
                    await session.commit()
                    print(f'Rooms left {rooms_left}')
                    return new_booking.mappings().one()
                else:
                    raise RoomFullyBookedException

        except RoomFullyBookedException:
            raise RoomFullyBookedException

    @classmethod
    async def get_email_info(
        cls,
        booking_id: int
    ):
        '''
        SELECT
        date_from,
        date_to,
        total_cost,
        total_days,
        hotels.name as hotel_name,
        rooms.name as hotel_room_name,
        rooms.description as hotel_room_description,
        rooms.services as hotel_room_services,
        hotels.location as hotel_location,
        hotels.services as hotel_services,
        users.email as user_email

        FROM bookings
        left JOIN
        rooms
        ON
        bookings.room_id = rooms.id
        LEFT JOIN
        hotels
        on
        rooms.hotel_id = hotels.id
        left JOIN
        users
        on
        bookings.user_id = users.id
        where
        users.email = 'fedor@moloko.ru'
        ;
        '''

        get_mail_info = select(
            Bookings.date_from,
            Bookings.date_to,
            Bookings.total_cost,
            Bookings.total_days,
            Hotels.name.label('hotel_name'),
            Rooms.name.label('hotel_room_name'),
            Rooms.description.label('hotel_room_description'),
            Rooms.services.label('hotel_room_services'),
            Hotels.location.label('hotel_location'),
            Hotels.services.label('hotel_services'),
            Users.email.label('user_email')
        ).select_from(Bookings) \
            .outerjoin(Rooms, Bookings.room_id == Rooms.id) \
            .outerjoin(Hotels, Rooms.hotel_id == Hotels.id) \
            .outerjoin(Users, Bookings.user_id == Users.id) \
            .where(Bookings.id == booking_id)

        async with async_session_maker() as session:
            user_bookings = await session.execute(get_mail_info)

            return user_bookings.mappings().one()

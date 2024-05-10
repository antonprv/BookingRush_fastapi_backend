from fastapi import APIRouter, Request, Depends

from fastapi_cache.decorator import cache
from pydantic import TypeAdapter

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking, SNewBooking
from app.users.models import Users
from app.users.dependencies import get_current_user
from app import exceptions as ex
from app.config import settings
from app.tasks.tasks import send_booking_confirmation
from app.tasks.email_templates import create_booking_confirmation_template
from app.bookings.schemas import SDictBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования']
)


@router.get('/all')
@cache(expire=settings.CACHE_EXPIRE)
async def get_bookings():
    return await BookingsDAO.find_all()


@router.get('/all/{user_id}')
@cache(expire=settings.CACHE_EXPIRE)
async def watch_per_user(user_id: int):
    return await BookingsDAO.find_all(user_id=user_id)


@router.post('/add')
async def add_booking(
        booking: SNewBooking,
        user: Users = Depends(get_current_user),
):
    booking = await BookingsDAO.add(
        user_id=user.id,
        room_id=booking.room_id,
        date_from=booking.date_from,
        date_to=booking.date_to
    )

    email_info = await BookingsDAO.get_email_info(booking_id=booking.id)
    email_info_dict = TypeAdapter(dict).validate_python(email_info)

    send_booking_confirmation.delay(
        email_info_dict=email_info_dict, email_to=user.email)

    return email_info_dict


@router.get('/')
@cache(expire=settings.CACHE_EXPIRE)
async def get_all_my_bookings(
        user: Users = Depends(get_current_user)
):
    return await BookingsDAO.find_all_for_user(user_id=user.id)


@router.delete('/{booking_id}')
async def delete_booking(
        booking_id: int,
        user: Users = Depends(get_current_user)
):
    await BookingsDAO.delete(id=booking_id, user_id=user.id)
    return {'message': 'booking deleted'}

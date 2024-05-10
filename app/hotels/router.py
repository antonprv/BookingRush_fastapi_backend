import asyncio

from fastapi import APIRouter, Depends

from fastapi_cache.decorator import cache

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotelsFindAll, SHotelsFindAllPayload, \
    SHotelsFindOne
from app.exceptions import HotelsNotFoundException
from app.config import settings

router = APIRouter(
    prefix='/hotels',
    tags=['Hotels']
)


@router.get('')
@cache(expire=settings.CACHE_EXPIRE)
async def get_hotels_by_location_and_time(
    payload: SHotelsFindAllPayload = Depends()
) -> list[SHotelsFindAll]:

    # await asyncio.sleep(3)

    hotels = await HotelsDAO.find_all(
        location=payload.location,
        date_from=payload.date_from,
        date_to=payload.date_to
    )

    if not hotels:
        raise HotelsNotFoundException

    return hotels


# Might be useful for the frontend
@router.get('/id/{hotel_id}')
@cache(expire=settings.CACHE_EXPIRE)
async def get_single_hotel(hotel_id: int) -> SHotelsFindOne:
    return await HotelsDAO.find_by_id(model_id=hotel_id)

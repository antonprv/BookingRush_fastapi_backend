from app.hotels.router import router
from app.hotels.rooms.schemas import SRoomsFindAll, SRoomsFindAllPayload
from app.hotels.rooms.dao import RoomsDAO
from app.exceptions import RoomsNotFoundException


@router.post('/{hotel_id}/rooms')
async def find_rooms(
        hotel_id: int,
        payload: SRoomsFindAllPayload
) -> SRoomsFindAll:

    rooms = await RoomsDAO.find_all(
        hotel_id=hotel_id,
        date_from=payload.date_from,
        date_to=payload.date_to
    )

    if not rooms:
        raise RoomsNotFoundException
    else:
        return rooms

from datetime import date

from pydantic import BaseModel


class SHotelsFindAll(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int
    rooms_left: int


class SHotelsFindAllPayload(BaseModel):
    location: str
    date_from: date
    date_to: date


class SHotelsFindOne(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

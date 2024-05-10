from datetime import date

from pydantic import BaseModel, EmailStr


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True


class SNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

    class Config:
        from_attributes = True


class SDictBooking(BaseModel):
    date_from: date
    date_to: date
    total_cost: int
    total_days: int
    hotel_name: str
    hotel_room_name: str
    hotel_room_description: str
    hotel_room_services: list[str]
    hotel_location: str
    hotel_services: list[str]
    user_email: EmailStr

from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserSecure(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str

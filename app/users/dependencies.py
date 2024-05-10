from datetime import datetime, UTC

from fastapi import Request, Depends
from jose import jwt, JWTError

from app.config import settings
from app.users.dao import UsersDAO
from app import exceptions as ex


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise ex.AbsentTokenException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token=token, key=settings.PW_KEY, algorithms=settings.PW_ALGORITHM
        )
    except JWTError:
        raise ex.IncorrectTokenFormatException

    expire: int = int(payload.get('exp'))
    if (not expire) or (expire < datetime.now(UTC).timestamp()):
        raise ex.ExpiredTokenException

    user_id: int = int(payload.get('sub'))
    if not user_id:
        raise ex.UserIsNotPresentException

    user = await UsersDAO.find_by_id(model_id=user_id)
    if not user:
        raise ex.UserIsNotPresentException

    return user

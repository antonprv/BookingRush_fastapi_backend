from typing import Union

from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import Users
from app.users.schemas import SUserSecure


# По умолчанию всегда возвращает ORM-класс без пароля.
# Для получения пароля - специальный метод get_hashed_password.
# При попытке вызвать пароль через user.hashed_password вернёт None.
class UsersDAO(BaseDAO):
    model: Users = Users

    class _Users:
        hashed_password = None

        def __init__(self, id: int, email: str):
            self.id = int(id)
            self.email = str(email)

    @classmethod
    async def find_by_id(cls, model_id: int) -> SUserSecure:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            result = result.scalar_one_or_none()

            if not result:
                return None
            else:
                user = cls._Users(id=result.id, email=result.email)
                return user

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> SUserSecure:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            result = result.scalar_one_or_none()

            if not result:
                return None
            else:
                user = cls._Users(id=result.id, email=result.email)
                return user

    @classmethod
    async def get_hashed_password(cls, **filter_by) -> Union[None, str]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            result = result.scalar_one_or_none()

            if result is None:
                return None
            else:
                return result.hashed_password

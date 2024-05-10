from typing import Any

from sqlalchemy import Column, Integer, String, JSON, ForeignKey, \
    Computed
from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

from pydantic import BaseModel

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String


# Модели Pydantic (Валидация данных)
class UserPy(BaseModel):
    username: str 
    password: str 


# Модели SqlAlchemy
class Base(AsyncAttrs, DeclarativeBase):
    ...

class UsersSQL(Base):
    __tablename__ = "Users"

    # Ограничение длины не работает надо будет переключиться на postgres
    username: Mapped[str] = mapped_column(String(length=32), primary_key = True, nullable = False)
    password: Mapped[str] = mapped_column(String(length=64))
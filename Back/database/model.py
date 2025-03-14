import os, sys, hashlib, hmac
sys.path.append(os.getcwd())

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import String, Integer, Sequence, select, and_, exc
from fastapi import HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv


# Запуск асинхронного движка для взаимодествия с БД
load_dotenv()
engine = create_async_engine(url = getenv("DBROOT"))
async_session = async_sessionmaker(engine, expire_on_commit = True)


# Модели Pydantic (Валидация данных)
class UserPy(BaseModel):
    username: str 
    password: str 


# Модели SqlAlchemy
class Base(AsyncAttrs, DeclarativeBase):
    ...

class UsersSQL(Base):
    __tablename__ = "Users"

    user_ID: Mapped[int] = mapped_column(Integer, primary_key = True, nullable = False, autoincrement = True)
    username: Mapped[str] = mapped_column(String(32))
    password: Mapped[str] = mapped_column(String(128))

    # Добавление в БД
    async def Create_User(user: UserPy) -> None | Exception:
        """Создание нового пользователя"""
        async with async_session() as session:
            try:
                hash_byte = hmac.new(getenv("HASH_KEY").encode(), user.password.encode(), hashlib.sha256)
                hex_dig = hash_byte.hexdigest()
                new_record = UsersSQL(username = user.username, password = hex_dig)
                session.add(new_record)
                await session.commit()
                await session.refresh(new_record)

            except Exception as e:
                await session.rollback()
                raise HTTPException(status_code = 400, detail = "Error while creating User: ")
            
            finally:
                await session.close()


    async def Get_User_ID(user: UserPy) -> Sequence[int] | Exception:
        """Получаем пользователя из БД"""
        async with async_session() as session:
            try:
                query = select(UsersSQL.user_ID).filter(and_(UsersSQL.username == user.username))
                result = await session.execute(query)

            except exc.SQLAlchemyError:
                await session.rollback()
                raise HTTPException(status_code = 400, detail = "SQLAlchemy Exception: ")
            
            except Exception:
                await session.rollback()
                raise HTTPException(status_code = 400, detail = "Error while getting User_ID: ")
            
            else:
                workers = result.scalars().all()
                return workers
            
            finally:
                await session.close()


# Запуск асинхронного движка
async def async_main():
    """Обновление данных в соответствии с metadata"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
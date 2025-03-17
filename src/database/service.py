import hashlib, hmac

from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, DataError

from dotenv import load_dotenv
from os import getenv

from ..models import UserPy, UsersSQL

from .core import async_session

# Parse a .env file and then load all the variables found as environment variables.
load_dotenv()


class DataBaseService:
    # Добавление в БД
    async def create_user(user: UserPy) -> None | Exception:
        """Создание нового пользователя"""
        async with async_session() as session:
            try:
                if len(user.username) > 32:
                    raise HTTPException(status_code = 400, detail = "Data error")
                
                hash_byte = hmac.new(getenv("HASH_KEY").encode(), user.password.encode(), hashlib.sha256)
                hex_dig = hash_byte.hexdigest()
                new_record = UsersSQL(username = user.username, password = hex_dig)
                session.add(new_record)
                await session.commit()
                await session.refresh(new_record)

            except IntegrityError as e:
                await session.rollback()
                raise HTTPException(status_code = 409, detail = "User already exist") from e
            
            except DataError as e: 
                await session.rollback()
                raise HTTPException(status_code = 400, detail = "Data error") from e

            except Exception as e:
                await session.rollback()
                raise HTTPException(status_code = 500, detail = "Unknown error") from e

    # Получение из БД
    async def get_user_id(user: UserPy) -> str | None:
        """Получаем пользователя из БД"""
        async with async_session() as session:
            try:
                query = select(UsersSQL.username).where(UsersSQL.username == user.username)
                result = await session.scalars(query)
                
            except SQLAlchemyError:
                await session.rollback()
                raise HTTPException(status_code = 500, detail = "SQLAlchemy Exception") from e
            
            except Exception as e:
                await session.rollback()
                raise HTTPException(status_code = 500, detail = f"Unexpected error: {str(e)}") from e
            
            else:
                entity = result.first()
                if entity == None:
                    raise HTTPException(status_code = 404, detail = "Entity doesn`t exist")
                return entity
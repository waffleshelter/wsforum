from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from dotenv import load_dotenv
from os import getenv

from ..models import Base

# Parse a .env file and then load all the variables found as environment variables.
load_dotenv()

# Описание движка
engine = create_async_engine(url = getenv("DBROOT"))
async_session = async_sessionmaker(engine, expire_on_commit = True)

# Запуск асинхронного движка
async def async_main():
    """Обновление данных в соответствии с metadata"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
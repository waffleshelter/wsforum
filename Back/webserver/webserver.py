import os, sys
sys.path.append(os.getcwd())

from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from web_post import router as POST
from web_get import router as GET
from Back.database.model import async_main
import uvicorn


# Менеджер жизненного цикла приложения (логирование и процессы)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Open")
    load_dotenv()
    await async_main() 
    yield # При отключении все что ниже
    print("Close")


# Инстанция нашего приложения FastAPI
app = FastAPI(lifespan = lifespan)
app.include_router(POST)
app.include_router(GET)


if __name__ == "__main__":
    uvicorn.run("webserver:app", host="127.0.0.1", port=8000)
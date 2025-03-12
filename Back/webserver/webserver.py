from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from web_post import router as POST
import uvicorn


# Менеджер жизненного цикла приложения (логирование и процессы)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Open") 
    load_dotenv()
    yield # При отключении все что ниже
    print("Close")


# Инстанция нашего приложения FastAPI
app = FastAPI(lifespan = lifespan)
app.include_router(POST)
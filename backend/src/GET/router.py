from fastapi import APIRouter, Response
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from os import getenv


# Роутер нашего FastAPI приложения
router = APIRouter()
load_dotenv()
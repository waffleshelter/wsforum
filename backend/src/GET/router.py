from fastapi import APIRouter, Response
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from os import getenv


# Роутер нашего FastAPI приложения
router = APIRouter()
load_dotenv()


@router.get("/", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse(f"{getenv("FPATH")}index.html")
    except Exception as e:
        return Response(content = "Unknown error", status_code = 500)


@router.get("/css/style.css", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse(f"{getenv("FPATH")}css/style.css")
    except Exception as e:
        return Response(content = "Unknown error", status_code = 500)


@router.get("/script.js", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse(f"{getenv("FPATH")}/script.js")
    except Exception as e:
        return Response(content = "Unknown error", status_code = 500)


@router.get("/imgs/close.svg", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse(f"{getenv("FPATH")}imgs/close.svg")
    except Exception as e:
        return Response(content = "Unknown error", status_code = 500)
    
    
@router.get("/favicon.ico", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse(f"{getenv("FPATH")}css/style.css")
    except Exception as e:
        return Response(content = "Unknown error", status_code = 500)
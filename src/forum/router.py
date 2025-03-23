from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

# Роутер нашего FastAPI приложения
router = APIRouter()

@router.get("/", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse("src/Front/index.html")
    except Exception as e:
        print(e)
        return Response(content = "Unknown error", status_code = 500)


@router.get("/css/style.css", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse("src/Front/css/style.css")
    except Exception as e:
        print(e)
        return Response(content = "Unknown error", status_code = 500)


@router.get("/script.js", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse("src/Front/script.js")
    except Exception as e:
        print(e)
        return Response(content = "Unknown error", status_code = 500)


@router.get("/imgs/close.svg", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse("src/Front/imgs/close.svg")
    except Exception as e:
        print(e)
        return Response(content = "Unknown error", status_code = 500)
    
    
@router.get("/favicon.ico", tags = ["Сайт"], summary = "Обработка запросов", status_code = 200)
async def Receive_data():
    try:
        return FileResponse("src/Front/imgs/close.svg")
    except Exception as e:
        print(e)
        return Response(content = "Unknown error", status_code = 500)
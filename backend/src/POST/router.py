from fastapi import APIRouter, Response, HTTPException

from ..logger import logger

from ..models import UserPy

from ..database.service import DataBaseService

# Роутер нашего FastAPI приложения
router = APIRouter()

@router.get("/get", tags = ["POST"], summary = "Обработка запросов")
async def receive_data():
    try:
        return "hello"
    except HTTPException as e:
        return Response(content = "Unknown error", status_code = e.status_code)

@router.post("/add", tags = ["POST"], summary = "Обработка запросов", status_code = 201)
async def receive_data(user: UserPy):
    try:
        await DataBaseService.create_user(user)
        logger.info("User succefuly created")
    except HTTPException as e:
        if e.status_code == 409:
            logger.error("User already exist")
            return Response(content = e.detail, status_code = e.status_code)
        logger.error(f"{e.detail}")
        return Response(content = "Unknown error", status_code = e.status_code)
        
@router.post("/get", tags = ["POST"], summary = "Обработка запросов", status_code = 200)
async def receive_data(user: UserPy):
    try:
        username = await DataBaseService.get_user_id(user)
    except HTTPException as e:
        logger.error("Unknown error")
        return Response(content = "Error", status_code = e.status_code) 
    else:
        logger.info("User succefuly created")
        return {"username": username}
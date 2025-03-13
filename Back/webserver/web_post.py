import os, sys
sys.path.append(os.getcwd())

from Back.database.model import UserPy, UsersSQL
from fastapi import APIRouter, Response, HTTPException


# Роутер нашего FastAPI приложения
router = APIRouter()


# Прием POST запроса
@router.post("/add", tags = "1", summary = "Обработка запросов", status_code = 201)
async def Receive_data(user: UserPy):
    try:
        await UsersSQL.Create_User(user)
    except HTTPException as e:
        return e.status_code


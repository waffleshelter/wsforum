import os, sys, logging
sys.path.append(os.getcwd())

from Back.database.model import UserPy, UsersSQL
from fastapi import APIRouter, Response, HTTPException


# Роутер нашего FastAPI приложения
router = APIRouter()
# Логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# Прием POST запроса
@router.post("/add", tags = ["POST"], summary = "Обработка запросов", status_code = 201)
async def Receive_data(user: UserPy):
    try:
        await UsersSQL.Create_User(user)
        logger.info("User succefuly created")
    except HTTPException as e:
        logger.error(f"{e.status_code}\n{e.detail}", exc_info=True)
        return e.status_code
    
@router.post("/get", tags = ["POST"], summary = "Обработка запросов", status_code = 200)
async def Receive_data(user: UserPy):
    try:
        user_id = await UsersSQL.Get_User_ID(user)
        logger.info("User succefuly find")
        return {"user_id": user_id}
    except HTTPException as e:
        logger.error(f"{e.status_code}\n{e.detail}", exc_info=True)
        return e.status_code
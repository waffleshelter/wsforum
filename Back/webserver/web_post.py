from fastapi import Request, APIRouter
from pydantic import BaseModel, SecretStr

# Роутер нашего FastAPI приложения
router = APIRouter()


# Модели Pydantic (Валидация данных)
class User(BaseModel):
    username: str 
    password: SecretStr


# Прием POST запроса
@router.post("/test", tags="1", summary="Обработка запросов")
async def Receive_data(user: User):
    return user
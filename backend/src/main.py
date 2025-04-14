from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from .POST.router import router as POST
from .GET.router import router as GET
from .database.core import async_main

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Open")
    load_dotenv()
    await async_main() 
    yield 
    print("Close")


app = FastAPI(lifespan = lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)
app.include_router(POST)
app.include_router(GET)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000)

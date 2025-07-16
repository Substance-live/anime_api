from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from src.api import main_router
from src.db import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await delete_tables()

app = FastAPI()
app.include_router(main_router)

origins = [
    "http://localhost",  # адрес фронтенда
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # разрешённые источники
    allow_credentials=True,
    allow_methods=["*"],  # разрешить все HTTP методы
    allow_headers=["*"],  # разрешить все заголовки
)

@app.post("/api/auth/login/")
def auth():
    return {
  "user": {
    "id": 1,
    "username": "user1"
  },
  "token": "jwt_or_session_token"
}

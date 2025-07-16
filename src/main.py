from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.api import main_router
from src.db import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await delete_tables()

app = FastAPI(lifespan=lifespan)
app.include_router(main_router)

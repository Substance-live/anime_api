import pytest_asyncio
from sqlalchemy import delete

from src.anime.models import AnimeOrm
from src.db import Session_maker, create_tables, delete_tables


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db():
    await delete_tables()
    await create_tables()


@pytest_asyncio.fixture
async def session():
    async with Session_maker() as session:
        yield session



@pytest_asyncio.fixture
async def delete_after(session):
    yield
    print("\nDeleting all data...")
    async with Session_maker() as session:
        query = delete(AnimeOrm)
        await session.execute(query)
        await session.commit()

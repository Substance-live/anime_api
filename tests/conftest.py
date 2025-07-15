import pytest
from sqlalchemy import delete

from src.anime.models import Anime
from src.db import Base, engine, Session_maker


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture
def session():
    return Session_maker()


@pytest.fixture
def delete_after(session):
    yield
    print("\nDeleting all data...")
    query = delete(Anime)
    session.execute(query)
    session.commit()

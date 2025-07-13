import pytest

from src.db import Base, engine, Session_maker


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

@pytest.fixture
def session():
    return Session_maker()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.config import settings

engine = create_engine(settings.DB_URL)
Session_maker = sessionmaker(engine)

class Base(DeclarativeBase):
    ...

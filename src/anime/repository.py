from typing import Sequence

from sqlalchemy import select, update, delete, func

from src.anime.models import Anime as AnimeORM
from src.db import Session_maker


class AnimeRepository:

    @classmethod
    def add(cls, value: dict) -> AnimeORM:
        with Session_maker() as session:
            new_anime = AnimeORM(**value)
            session.add(new_anime)
            session.commit()
            session.refresh(new_anime)
            return new_anime

    @classmethod
    def get(cls, value_id) -> AnimeORM | None:
        with Session_maker() as session:
            return session.get(AnimeORM, value_id)

    @classmethod
    def list(cls, filter_by: dict) -> Sequence[AnimeORM]:
        with Session_maker() as session:
            if filter_by is None:
                filter_by = {}

            query = select(AnimeORM).filter_by(**filter_by)
            return session.scalars(query).all()

    @classmethod
    def update(cls, value_id: int, values: dict):
        with Session_maker() as session:
            query = update(AnimeORM).where(AnimeORM.id == value_id).values(**values)
            session.execute(query)
            session.commit()

    @classmethod
    def delete(cls, value_id: int):
        with Session_maker() as session:
            query = delete(AnimeORM).where(AnimeORM.id == value_id)
            session.execute(query)
            session.commit()

    @classmethod
    def count(cls) -> int:
        with Session_maker() as session:
            query = select(func.count(AnimeORM.id)).select_from(AnimeORM)
            ret = session.execute(query)
            return ret.scalar()

    @classmethod
    def delete_all(cls):
        with Session_maker() as session:
            query = delete(AnimeORM)
            session.execute(query)
            session.commit()

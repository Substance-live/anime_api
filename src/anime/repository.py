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
            ret = session.get(AnimeORM, value_id)

            if ret is None:
                raise IndexError

            return ret

    @classmethod
    def list(cls, filter_by: dict = None) -> Sequence[AnimeORM]:
        if filter_by is None:
            filter_by = {}

        with Session_maker() as session:
            if filter_by is None:
                filter_by = {}

            query = select(AnimeORM).filter_by(**filter_by)
            return session.scalars(query).all()

    @classmethod
    def update(cls, value_id: int, values: dict) -> int:
        with Session_maker() as session:
            query = update(AnimeORM).where(AnimeORM.id == value_id).values(**values)
            ret = session.execute(query)
            session.commit()
            return ret.rowcount

    @classmethod
    def delete(cls, value_id: int) -> int:
        with Session_maker() as session:
            query = delete(AnimeORM).where(AnimeORM.id == value_id)
            ret = session.execute(query)
            session.commit()
            return ret.rowcount

    @classmethod
    def count(cls) -> int:
        with Session_maker() as session:
            query = select(func.count(AnimeORM.id)).select_from(AnimeORM)
            ret = session.execute(query)
            return ret.scalar()

    @classmethod
    def delete_all(cls) -> int:
        with Session_maker() as session:
            query = delete(AnimeORM)
            ret = session.execute(query)
            session.commit()
            return ret.rowcount

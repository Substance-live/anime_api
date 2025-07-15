from typing import Sequence

from sqlalchemy import select, update, delete, func

from src.anime.models import AnimeOrm
from src.db import Session_maker


class AnimeRepository:

    @classmethod
    async def add(cls, value: dict) -> AnimeOrm:
        async with Session_maker() as session:
            new_anime = AnimeOrm(**value)
            session.add(new_anime)
            await session.commit()
            await session.refresh(new_anime)
            return new_anime

    @classmethod
    async def get(cls, value_id) -> AnimeOrm | None:
        async with Session_maker() as session:
            ret = await session.get(AnimeOrm, value_id)

            if ret is None:
                raise IndexError

            return ret

    @classmethod
    async def list(cls, filter_by: dict = None) -> Sequence[AnimeOrm]:
        if filter_by is None:
            filter_by = {}

        async with Session_maker() as session:
            if filter_by is None:
                filter_by = {}

            query = select(AnimeOrm).filter_by(**filter_by)
            return (await session.scalars(query)).all()

    @classmethod
    async def update(cls, value_id: int, values: dict) -> int:
        async with Session_maker() as session:
            query = update(AnimeOrm).where(AnimeOrm.id == value_id).values(**values)
            ret = await session.execute(query)
            await session.commit()
            return ret.rowcount

    @classmethod
    async def delete(cls, value_id: int) -> int:
        async with Session_maker() as session:
            query = delete(AnimeOrm).where(AnimeOrm.id == value_id)
            ret = await session.execute(query)
            await session.commit()
            return ret.rowcount

    @classmethod
    async def count(cls) -> int:
        async with Session_maker() as session:
            query = select(func.count(AnimeOrm.id)).select_from(AnimeOrm)
            ret = await session.execute(query)
            return ret.scalar()

    @classmethod
    async def delete_all(cls) -> int:
        async with Session_maker() as session:
            query = delete(AnimeOrm)
            ret = await session.execute(query)
            await session.commit()
            return ret.rowcount

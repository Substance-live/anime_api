from src.anime.repository import AnimeRepository
from src.anime.schemas import AnimeSchema, AnimeCreateSchema

class AnimeService:

    @classmethod
    async def add(cls, anime_in: AnimeCreateSchema) -> AnimeSchema:
        anime_value = anime_in.model_dump()
        db_anime = await AnimeRepository.add(anime_value)
        return AnimeSchema.model_validate(db_anime)

    @classmethod
    async def get(cls, anime_id: int) -> AnimeSchema:
        db_anime = await AnimeRepository.get(anime_id)
        return AnimeSchema.model_validate(db_anime)

    @classmethod
    async def list(cls, filter_by: dict = None) -> list[AnimeSchema]:
        db_anime_seq = await AnimeRepository.list(filter_by)
        return [AnimeSchema.model_validate(elem) for elem in db_anime_seq]

    @classmethod
    async def update(cls, anime_id: int, anime_update: AnimeSchema | AnimeCreateSchema) -> int:
        anime_value = anime_update.model_dump()
        return await AnimeRepository.update(anime_id, anime_value)

    @classmethod
    async def delete(cls, anime_id: int) -> int:
        return await AnimeRepository.delete(anime_id)

    @classmethod
    async def count(cls) -> int:
        return await AnimeRepository.count()

    @classmethod
    async def delete_all(cls) -> int:
        return await AnimeRepository.delete_all()
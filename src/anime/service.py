from sqlalchemy.orm import Session

from src.anime.repository import AnimeRepository
from src.anime.schemas import AnimeSchema, AnimeCreateSchema

class AnimeService:

    @classmethod
    def add(cls,anime_in: AnimeCreateSchema) -> AnimeSchema:
        anime_value = anime_in.model_dump(exclude_unset=True)
        db_anime = AnimeRepository.add(anime_value)
        return AnimeSchema.model_validate(db_anime)

    @classmethod
    def get(cls,anime_id: int) -> AnimeSchema:
        db_anime = AnimeRepository.get(anime_id)
        return AnimeSchema.model_validate(db_anime)

    @classmethod
    def list(cls,filter_by: dict = None) -> list[AnimeSchema]:
        db_anime_seq = AnimeRepository.list(filter_by)
        return [AnimeSchema.model_validate(elem) for elem in db_anime_seq]

    @classmethod
    def update(cls,anime_id: int, anime_update: AnimeSchema):
        anime_value = anime_update.model_dump(exclude_unset=True)
        AnimeRepository.update(anime_id, anime_value)

    @classmethod
    def delete(cls,anime_id: int):
        AnimeRepository.delete(anime_id)

    @classmethod
    def count(cls) -> int:
        return AnimeRepository.count()

    @classmethod
    def delete_all(cls):
        AnimeRepository.delete_all()
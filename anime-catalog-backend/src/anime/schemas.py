from pydantic import BaseModel, ConfigDict

from src.anime.enum.anime_status import AnimeStatus

class AnimeBaseSchema(BaseModel):
    title: str
    status: AnimeStatus
    description: str
    genres: list[str]

class AnimeCreateSchema(AnimeBaseSchema):
    ...

class AnimeSchema(AnimeBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes = True)


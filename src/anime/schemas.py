from pydantic import BaseModel, ConfigDict

from src.anime.enum.anime_status import AnimeStatus

class AnimeBaseSchema(BaseModel):
    title: str
    episodes: int
    status: AnimeStatus
    genre: str | None

class AnimeCreateSchema(AnimeBaseSchema):
    ...

class AnimeSchema(AnimeBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes = True)


from pydantic import BaseModel

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

    class Config:
        from_attributes = True

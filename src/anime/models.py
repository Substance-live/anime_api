from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.anime.enum.anime_status import AnimeStatus


class AnimeOrm(Base):
    __tablename__ = "anime"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    episodes: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(SqlEnum(AnimeStatus, name="anime_status"), nullable=False)
    genre: Mapped[str]

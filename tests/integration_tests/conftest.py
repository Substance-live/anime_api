import pytest

from src.anime.enum.anime_status import AnimeStatus
from src.anime.schemas import AnimeCreateSchema


@pytest.fixture
def anime_model():
    anime = [
        AnimeCreateSchema(title='Naruto', episodes=355, status=AnimeStatus.completed, genre='senen'),
        AnimeCreateSchema(title='Onepiece', episodes=1111, status=AnimeStatus.ongoing, genre='senen'),
        AnimeCreateSchema(title='Death note', episodes=42, status=AnimeStatus.completed, genre='detective'),
        AnimeCreateSchema(title='Demon slayer final', episodes=1, status=AnimeStatus.announced, genre='fantasy'),
    ]
    return anime


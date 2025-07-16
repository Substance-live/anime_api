import pytest

from src.anime.enum.anime_status import AnimeStatus
from src.anime.schemas import AnimeCreateSchema


@pytest.fixture
def anime_model():
    anime = [
        AnimeCreateSchema(title='Naruto', status=AnimeStatus.completed, genres=['senen', 'also genres'], description="Just description"),
        AnimeCreateSchema(title='Onepiece', status=AnimeStatus.ongoing, genres=['senen', 'also genres'], description="Just description"),
        AnimeCreateSchema(title='Death note', status=AnimeStatus.completed, genres=['detective', 'also genres'], description="Just description"),
        AnimeCreateSchema(title='Demon slayer final', status=AnimeStatus.announced, genres=['fantasy', 'also genres'], description="Just description"),
    ]
    return anime


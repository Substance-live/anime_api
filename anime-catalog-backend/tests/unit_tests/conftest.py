import pytest_asyncio
import pytest

from src.anime.enum.anime_status import AnimeStatus
from src.anime.models import AnimeOrm


@pytest.fixture
def anime_dict():
    anime = [
        {'title': 'Naruto', 'status': AnimeStatus.completed, 'genres': ['senen', 'also genres'], 'description': "Just description"},
        {'title': 'Onepiece', 'status': AnimeStatus.ongoing, 'genres': ['senen', 'also genres'], 'description': "Just description"},
        {'title': 'Death note', 'status': AnimeStatus.completed, 'genres': ['detective', 'also genres'], 'description': "Just description"},
        {'title': 'Demon slayer final', 'status': AnimeStatus.announced, 'genres': ['fantasy', 'also genres'], 'description': "Just description"}
    ]
    return anime


@pytest_asyncio.fixture
async def load_data(session, anime_dict):
    for value in anime_dict:
        new_anime = AnimeOrm(**value)
        session.add(new_anime)
        await session.commit()

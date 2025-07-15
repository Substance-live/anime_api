import pytest_asyncio
import pytest

from src.anime.enum.anime_status import AnimeStatus
from src.anime.models import AnimeOrm


@pytest.fixture
def anime_dict():
    anime = [
        {'title': 'Naruto', 'episodes': 355, 'status': AnimeStatus.completed, 'genre': 'senen'},
        {'title': 'Onepiece', 'episodes': 1111, 'status': AnimeStatus.ongoing, 'genre': 'senen'},
        {'title': 'Death note', 'episodes': 42, 'status': AnimeStatus.completed, 'genre': 'detective'},
        {'title': 'Demon slayer final', 'episodes': 1, 'status': AnimeStatus.announced, 'genre': 'fantasy'}
    ]
    return anime


@pytest_asyncio.fixture
async def load_data(session, anime_dict):
    for value in anime_dict:
        new_anime = AnimeOrm(**value)
        session.add(new_anime)
        await session.commit()

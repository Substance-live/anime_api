import pytest
from sqlalchemy import delete

from src.anime.enum.anime_status import AnimeStatus
from src.anime.models import Anime


@pytest.fixture
def anime_dict():
    anime = [
        {'title': 'Naruto', 'episodes': 355, 'status': AnimeStatus.completed, 'genre': 'senen'},
        {'title': 'Onepiece', 'episodes': 1111, 'status': AnimeStatus.ongoing, 'genre': 'senen'},
        {'title': 'Death note', 'episodes': 42, 'status': AnimeStatus.completed, 'genre': 'detective'},
        {'title': 'Demon slayer final', 'episodes': 1, 'status': AnimeStatus.announced, 'genre': 'fantasy'}
    ]
    return anime

@pytest.fixture
def delete_after(session):
    yield
    print("\nDeleting all data...")
    query = delete(Anime)
    session.execute(query)
    session.commit()


@pytest.fixture
def load_data(session, anime_dict):
    for value in anime_dict:
        new_anime = Anime(**value)
        session.add(new_anime)
        session.commit()

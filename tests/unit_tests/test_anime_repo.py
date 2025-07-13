from contextlib import nullcontext as does_not_raise

import pytest
from sqlalchemy import delete

from src.anime.enum.anime_status import AnimeStatus
from src.anime.models import Anime
from src.anime.repository import AnimeRepository
from tests.unit_tests.conftest import load_data


@pytest.mark.usefixtures("delete_after")
class TestRepository:

    @pytest.mark.parametrize(
        "input_dict, expectation",
        [
            ({'title': 'Naruto', 'episodes': 355, 'status': AnimeStatus.completed, 'genre': 'senen'},
             does_not_raise()),
            ({'title': "test", 'episodes': 1, 'status': AnimeStatus.ongoing, 'genre': 'test'},
             does_not_raise()),
            ({"wrong dict": None},
             pytest.raises(TypeError))
        ]
    )
    def test_add(self, input_dict, expectation):
        with expectation:
            added_anime = AnimeRepository.add(input_dict)

            assert 1 == added_anime.id
            assert input_dict["title"] == added_anime.title

    @pytest.mark.usefixtures("load_data")
    class TestWithStartData:

        @pytest.mark.parametrize(
            "input_id, expected_title, expectation",
            [
                (2, "Onepiece", does_not_raise()),
                (1, "Naruto", does_not_raise()),
                (4, "Demon slayer final", does_not_raise()),
                (5, None, pytest.raises(IndexError)),
            ]
        )
        def test_get_on_id(self, input_id, expected_title, expectation):
            with expectation:
                assert AnimeRepository.get(input_id).title == expected_title

        @pytest.mark.parametrize(
            "input_id, input_value, count_updated_rows",
            [
                (1, {'title': 'Boruto'}, 1),
                (3, {'genre': 'TestGenre'}, 1),
                (5, {'title': "TEST"}, 0)
            ]
        )
        def test_update(self, session, input_id, input_value, count_updated_rows):
            ret = AnimeRepository.update(input_id, input_value)

            assert ret == count_updated_rows

            if ret != 0:
                for attr in input_value.keys():
                    assert getattr(session.get(Anime, input_id), attr) == input_value[attr]

        @pytest.mark.parametrize(
            "input_id, count_deleted_rows",
            [
                (1, 1),
                (2, 1),
                (4, 1),
                (6, 0),
                (-1, 0),
            ]
        )
        def test_delete(self, session, input_id, count_deleted_rows):
            ret = AnimeRepository.delete(input_id)

            assert ret == count_deleted_rows
            assert session.get(Anime, input_id) is None

        @pytest.mark.parametrize(
            "filter_by, expected_output",
            [
                ({"status": AnimeStatus.completed}, [1, 3]),
                ({"status": AnimeStatus.announced}, [4]),
                ({"status": "announced"}, [4]),
                ({"status": "wrong value"}, []),
                ({"genre": "senen"}, [1, 2]),
                ({"genre": "detective"}, [3]),
                ({"genre": "wrong_value"}, []),
                ({"title": "Naruto"}, [1]),
                ({"title": "Death note"}, [3]),
                ({"title": "wrong value"}, []),
                ({"status": AnimeStatus.announced, "genre": "fantasy"}, [4]),
            ]
        )
        def test_filter_by(self, filter_by, expected_output):
            ret = AnimeRepository.list(filter_by)
            assert [orm_obj.id for orm_obj in ret] == expected_output

        def test_count(self, session):
            for index in range(1, 5):
                query = delete(Anime).where(Anime.id == index)
                session.execute(query)
                session.commit()

                assert (4 - index) == AnimeRepository.count()

from contextlib import nullcontext as does_not_raise

import pytest

from src.anime.enum.anime_status import AnimeStatus
from src.anime.schemas import AnimeSchema, AnimeCreateSchema
from src.anime.service import AnimeService


@pytest.mark.asyncio
@pytest.mark.usefixtures("delete_after")
class TestService:

    @pytest.mark.parametrize(
        "input_id, expectation",
        [
            (1, does_not_raise()),
            (3, does_not_raise()),
            (4, does_not_raise()),
            (5, pytest.raises(IndexError)),
            (0, pytest.raises(IndexError)),
            (-1, pytest.raises(IndexError)),
        ]
    )
    async def test_add_and_get(self, anime_model, input_id, expectation):
        with expectation:
            for model in anime_model:
                await AnimeService.add(model)

            assert [AnimeCreateSchema(**model.model_dump()) for model in await AnimeService.list()] == anime_model

            assert await AnimeService.get(input_id) == AnimeSchema(id=input_id, **anime_model[input_id - 1].model_dump())

    @pytest.mark.parametrize(
        "update_model, expectation",
        [
            (AnimeSchema(id=4, title="TestTitle", episodes=5, status=AnimeStatus.completed, genre="TestGenre"),
             does_not_raise()),
            (AnimeSchema(id=2, title='Naruto', episodes=355, status=AnimeStatus.completed, genre='senen'),
             does_not_raise()),
            (AnimeSchema(id=5, title="TestTitle", episodes=5, status=AnimeStatus.completed, genre="TestGenre"),
             pytest.raises(IndexError)),
            (AnimeSchema(id=0, title="TestTitle", episodes=5, status=AnimeStatus.completed, genre="TestGenre"),
             pytest.raises(IndexError)),

        ]
    )
    async def test_update(self, anime_model, update_model: AnimeSchema, expectation):
        with expectation:
            for model in anime_model:
                await AnimeService.add(model)

            count_update_rows = await AnimeService.update(update_model.id, update_model)

            assert count_update_rows == 1 or expectation != does_not_raise()

            assert await AnimeService.get(update_model.id) == update_model

    @pytest.mark.parametrize(
        "input_id",
        [
            1,
            2,
            3,
            4,
        ]
    )
    async def test_delete_right(self, anime_model, input_id):
        for model in anime_model:
            await AnimeService.add(model)

        assert await AnimeService.delete(input_id) == 1

        assert await AnimeService.count() == len(anime_model) - 1

        with pytest.raises(IndexError):
            await AnimeService.get(input_id)

        anime_model.pop(input_id - 1)
        assert [AnimeCreateSchema(**model.model_dump()) for model in await AnimeService.list()] == anime_model

    @pytest.mark.parametrize(
        "input_id",
        [
            -1,
            0,
            5,
            -99,
        ]
    )
    async def test_delete_wrong(self, anime_model, input_id):
        for model in anime_model:
            await AnimeService.add(model)

        before_list = await AnimeService.list()
        count_del_rows = await AnimeService.delete(input_id)
        after_list = await AnimeService.list()

        assert before_list == after_list
        assert count_del_rows == 0

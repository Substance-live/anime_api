from fastapi import APIRouter, HTTPException

from src.anime.schemas import AnimeSchema, AnimeCreateSchema
from src.anime.service import AnimeService


router = APIRouter(
    prefix="/anime",
    tags=["Аниме"]
)

@router.get("")
async def get_anime(anime_id: int) -> AnimeSchema:
    try:
        ret = await AnimeService.get(anime_id)
    except IndexError:
        raise HTTPException(404, "Wrong anime_id")
    return ret

@router.get("/all")
async def get_all_anime(filter_by: dict | None = None) -> list[AnimeSchema]:
    ret = await AnimeService.list(filter_by)
    return ret

@router.put("")
async def update_anime(anime_id: int, anime_model: AnimeCreateSchema):
    ret = await AnimeService.update(anime_id, anime_model)
    return {"ok": ret == 1}

@router.delete("")
async def delete_anime(anime_id: int):
    ret = await AnimeService.delete(anime_id)
    return {"ok": ret == 1}

@router.delete("/all")
async def delete_all_anime():
    ret = await AnimeService.delete_all()
    return {"ok": ret == 1}

@router.get("/count")
async def get_count_anime() -> int:
    ret = await AnimeService.count()
    return ret

@router.post("")
async def post_anime(anime_model: AnimeCreateSchema) -> int:
    ret = await AnimeService.add(anime_model)
    return ret.id

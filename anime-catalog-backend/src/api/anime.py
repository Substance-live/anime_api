from typing import Optional

from fastapi import APIRouter, HTTPException

from src.anime.schemas import AnimeSchema, AnimeCreateSchema
from src.anime.service import AnimeService


router = APIRouter(
    prefix="/api/anime",
    tags=["Аниме"]
)

@router.get("/{anime_id}/")
async def get_anime(anime_id: int) -> AnimeSchema:
    try:
        ret = await AnimeService.get(anime_id)
    except IndexError:
        raise HTTPException(404, "Wrong anime_id")
    return ret

@router.get("/")
async def get_all_anime(genres: Optional[str] = None, status: Optional[str] = None) -> list[AnimeSchema]:


    filter_by = {}
    if genres:
        filter_by["genres"] = genres
    print("api before", filter_by)
    if status:
        filter_by["status"] = status
    print("api after", filter_by)
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

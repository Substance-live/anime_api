from fastapi import APIRouter

from src.api.anime import router as anime_router

main_router = APIRouter()
main_router.include_router(anime_router)

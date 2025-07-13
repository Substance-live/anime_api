from src.anime.schemas import AnimeCreateSchema, AnimeStatus
from src.anime.service import AnimeService

from src.db import Base, engine

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# anime_1 = AnimeCreateSchema(
#     title="Demon slayer final",
#     episodes=1,
#     status=AnimeStatus.announced,
#     genre="fantasy"
# )
# added_anime = AnimeService.add(session, anime_1)

all_anime = AnimeService.list()
print("\n".join([str(anime) for anime in all_anime]))
print(AnimeService.count())
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchAnimeDetail } from '../api/animeApi';
import AnimeDetail from '../components/AnimeDetail';
import { useUserLists } from '../context/UserListsContext';

export default function AnimePage() {
  const { id } = useParams();
  const [anime, setAnime] = useState(null);
  const { watchLater, setWatchLater, watched, setWatched, favorites, setFavorites } = useUserLists();

  useEffect(() => {
    fetchAnimeDetail(id).then(res => setAnime(res.data));
  }, [id]);

  function handleAddToList(list, anime) {
    if (list === 'watchLater') setWatchLater(prev => [...prev, anime]);
    if (list === 'watched') setWatched(prev => [...prev, anime]);
    if (list === 'favorites') setFavorites(prev => [...prev, anime]);
  }

  return (
    <div className="container">
      <AnimeDetail anime={anime} onAddToList={handleAddToList} />
    </div>
  );
} 
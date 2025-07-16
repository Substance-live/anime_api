import { useEffect, useState } from 'react';
import { fetchAnimeList } from '../api/animeApi';
import AnimeList from '../components/AnimeList';
import FilterBar from '../components/FilterBar';

const GENRES = ['senen', 'detective', 'fantasy', 'also genre']; // пример
const STATUSES = ['ongoing', 'completed', 'announced'];

export default function Home() {
  const [animeList, setAnimeList] = useState([]);
  const [genre, setGenre] = useState('');
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetchAnimeList({ genres: genre, status })
      .then(res => setAnimeList(res.data))
      .finally(() => setLoading(false));
  }, [genre, status]);

  return (
    <div className="container">
      <h1>Аниме каталог</h1>
      <FilterBar
        genres={GENRES}
        statuses={STATUSES}
        selectedGenre={genre}
        selectedStatus={status}
        onGenreChange={setGenre}
        onStatusChange={setStatus}
      />
      {loading ? <div>Загрузка...</div> : <AnimeList animeList={animeList} />}
    </div>
  );
} 
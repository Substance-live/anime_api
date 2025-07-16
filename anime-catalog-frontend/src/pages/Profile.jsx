import { useUserLists } from '../context/UserListsContext';
import AnimeList from '../components/AnimeList';

export default function Profile() {
  const { watchLater, watched, favorites } = useUserLists();
  return (
    <div className="container">
      <h2>Профиль</h2>
      <h3>Посмотрю позже</h3>
      <AnimeList animeList={watchLater} />
      <h3>Просмотрено</h3>
      <AnimeList animeList={watched} />
      <h3>Любимое</h3>
      <AnimeList animeList={favorites} />
    </div>
  );
} 
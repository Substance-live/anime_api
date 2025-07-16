import AnimeCard from './AnimeCard';

export default function AnimeList({ animeList, onAddToList }) {
  return (
    <div style={{display: 'flex', flexWrap: 'wrap', gap: 16}}>
      {animeList.map(anime => (
        <AnimeCard key={anime.id} anime={anime} onAddToList={onAddToList} />
      ))}
    </div>
  );
} 
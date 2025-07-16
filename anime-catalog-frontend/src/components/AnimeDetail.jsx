export default function AnimeDetail({ anime, onAddToList }) {
  if (!anime) return <div>Аниме не найдено</div>;
  return (
    <div style={{background: '#fff', borderRadius: 8, padding: 24, maxWidth: 600}}>
      <h2>{anime.title}</h2>
      <div><b>Жанры:</b> {anime.genres?.join(', ')}</div>
      <div><b>Статус:</b> {anime.status}</div>
      <div><b>Описание:</b> {anime.description}</div>
      {onAddToList && (
        <div style={{marginTop: 16}}>
          <button onClick={() => onAddToList('watchLater', anime)} style={{marginRight: 8}}>Посмотрю позже</button>
          <button onClick={() => onAddToList('watched', anime)} style={{marginRight: 8}}>Просмотрено</button>
          <button onClick={() => onAddToList('favorites', anime)}>Любимое</button>
        </div>
      )}
    </div>
  );
} 
import { Link } from 'react-router-dom';

export default function AnimeCard({ anime, onAddToList }) {
  return (
    <div style={{border: '1px solid #ddd', borderRadius: 8, padding: 16, background: '#fff', marginBottom: 16, width: 220}}>
      <Link to={`/anime/${anime.id}`} style={{textDecoration: 'none', color: '#222'}}>
        <h3 style={{margin: '0 0 8px 0'}}>{anime.title}</h3>
        <div style={{fontSize: 14, color: '#666'}}>{anime.genres?.join(', ')}</div>
        <div style={{fontSize: 13, color: '#888', margin: '8px 0'}}>{anime.status}</div>
      </Link>
      {onAddToList && (
        <div style={{marginTop: 8}}>
          <button onClick={() => onAddToList('watchLater', anime)} style={{marginRight: 8}}>Посмотрю позже</button>
          <button onClick={() => onAddToList('watched', anime)} style={{marginRight: 8}}>Просмотрено</button>
          <button onClick={() => onAddToList('favorites', anime)}>Любимое</button>
        </div>
      )}
    </div>
  );
} 
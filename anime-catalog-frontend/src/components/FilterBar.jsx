export default function FilterBar({ genres, statuses, selectedGenre, selectedStatus, onGenreChange, onStatusChange }) {
  return (
    <div style={{marginBottom: 24, display: 'flex', gap: 16}}>
      <select value={selectedGenre} onChange={e => onGenreChange(e.target.value)}>
        <option value="">Все жанры</option>
        {genres.map(g => <option key={g} value={g}>{g}</option>)}
      </select>
      <select value={selectedStatus} onChange={e => onStatusChange(e.target.value)}>
        <option value="">Все статусы</option>
        {statuses.map(s => <option key={s} value={s}>{s}</option>)}
      </select>
    </div>
  );
} 
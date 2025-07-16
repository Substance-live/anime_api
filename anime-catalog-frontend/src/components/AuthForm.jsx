import { useState } from 'react';

export default function AuthForm({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  return (
    <form onSubmit={e => { e.preventDefault(); onLogin({ username, password }); }} style={{maxWidth: 320, margin: '0 auto', background: '#fff', padding: 24, borderRadius: 8}}>
      <h2>Вход</h2>
      <div style={{marginBottom: 12}}>
        <input type="text" placeholder="Логин" value={username} onChange={e => setUsername(e.target.value)} required style={{width: '100%'}} />
      </div>
      <div style={{marginBottom: 12}}>
        <input type="password" placeholder="Пароль" value={password} onChange={e => setPassword(e.target.value)} required style={{width: '100%'}} />
      </div>
      <button type="submit" style={{width: '100%'}}>Войти</button>
    </form>
  );
} 
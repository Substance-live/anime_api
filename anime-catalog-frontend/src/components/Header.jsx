import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Header() {
  const { user } = useAuth();
  return (
    <header>
      <nav className="container" style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between'}}>
        <div>
          <Link to="/" style={{color: '#fff', textDecoration: 'none', fontWeight: 'bold', fontSize: 24}}>AnimeCatalog</Link>
        </div>
        <div>
          <Link to="/" style={{color: '#fff', marginRight: 16}}>Главная</Link>
          {user ? (
            <>
              <Link to="/profile" style={{color: '#fff', marginRight: 16}}>Профиль</Link>
              <span>{user.username}</span>
            </>
          ) : (
            <Link to="/login" style={{color: '#fff'}}>Войти</Link>
          )}
        </div>
      </nav>
    </header>
  );
} 
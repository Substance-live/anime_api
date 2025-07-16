import { useAuth } from '../context/AuthContext';
import AuthForm from '../components/AuthForm';
import { useNavigate } from 'react-router-dom';
import { login } from '../api/animeApi';

export default function Login() {
  const { setUser } = useAuth();
  const navigate = useNavigate();

  async function handleLogin(data) {
    try {
      const res = await login(data);
      setUser(res.data.user); // предполагается, что API возвращает user
      navigate('/');
    } catch (e) {
      alert('Ошибка входа');
    }
  }

  return (
    <div className="container">
      <AuthForm onLogin={handleLogin} />
    </div>
  );
} 
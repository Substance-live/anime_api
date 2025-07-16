import { AuthProvider } from './context/AuthContext';
import { UserListsProvider } from './context/UserListsContext';
import AppRouter from './router/AppRouter';
import Header from './components/Header';

export default function App() {
  return (
    <AuthProvider>
      <UserListsProvider>
        <Header />
        <AppRouter />
      </UserListsProvider>
    </AuthProvider>
  );
} 
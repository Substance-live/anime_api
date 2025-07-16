import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import AnimePage from '../pages/AnimePage';
import Login from '../pages/Login';
import Profile from '../pages/Profile';

export default function AppRouter() {
  return (
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/anime/:id" element={<AnimePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
  );
} 
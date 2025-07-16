import axios from 'axios';

const API_URL = '/api'; // Замените на ваш адрес

export const fetchAnimeList = (params) => axios.get(`${API_URL}/anime/`, { params });
export const fetchAnimeDetail = (id) => axios.get(`${API_URL}/anime/${id}/`);
export const login = (data) => axios.post(`${API_URL}/auth/login/`, data);
// Добавьте другие методы по необходимости 
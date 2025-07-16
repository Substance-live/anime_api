# Anime Catalog

Полноценное приложение для ведения личного каталога аниме (аналог shikimori.one), включающее backend на FastAPI и frontend на React + Vite.

## Структура проекта

```
pytest_anime/
├── anime-catalog-backend/   # Backend (FastAPI, SQLite)
│   ├── src/
│   │   ├── anime/           # Модели, сервисы, enum
│   │   ├── api/             # FastAPI роутеры
│   │   ├── main.py          # Точка входа
│   │   ├── db.py, config.py # Настройки и БД
│   ├── tests/               # Unit и integration тесты
│   ├── requirements.txt     # Зависимости
│   ├── Dockerfile
│   └── pytest.ini
├── anime-catalog-frontend/  # Frontend (React, Vite)
│   ├── src/
│   │   ├── api/             # Взаимодействие с backend
│   │   ├── components/      # UI-компоненты
│   │   ├── pages/           # Страницы
│   │   ├── context/         # React Context
│   │   ├── router/          # Роутинг
│   │   └── styles/          # Стили
│   ├── package.json         # Зависимости
│   ├── Dockerfile
│   └── vite.config.js
├── docker-compose.yml       # Запуск всего проекта
```

## Основной функционал
- Каталог аниме с фильтрами
- Просмотр подробной информации об аниме
- Авторизация пользователей
- Пользовательские списки: "Посмотрю позже", "Просмотрено", "Любимое"

## Быстрый старт

### Через Docker Compose
```bash
docker-compose up --build
```
- Backend будет доступен на порту 8000 (внутри сети)
- Frontend — на http://localhost (порт 80)

### Ручной запуск
#### Backend
```bash
cd anime-catalog-backend
pip install -r requirements.txt
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```
#### Frontend
```bash
cd anime-catalog-frontend
npm install
npm run dev
```

## Зависимости
### Backend (FastAPI)
- fastapi, uvicorn, sqlalchemy, aiosqlite, pydantic, pytest и др. (см. requirements.txt)

### Frontend (React)
- react, react-dom, react-router-dom, axios, vite (см. package.json)

## API
- Примеры эндпоинтов backend:
  - `GET /api/anime/` — список аниме (фильтры: жанр, статус)
  - `GET /api/anime/{id}/` — детали аниме
  - `POST /api/anime/` — добавить аниме
  - `PUT /api/anime/` — обновить аниме
  - `DELETE /api/anime/` — удалить аниме
  - `POST /api/auth/login/` — авторизация

## Контакты
Автор: Substance-live

---

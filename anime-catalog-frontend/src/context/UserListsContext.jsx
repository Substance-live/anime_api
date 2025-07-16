import { createContext, useContext, useState } from 'react';

const UserListsContext = createContext();

export const useUserLists = () => useContext(UserListsContext);

export function UserListsProvider({ children }) {
  const [watchLater, setWatchLater] = useState([]);
  const [watched, setWatched] = useState([]);
  const [favorites, setFavorites] = useState([]);
  // Методы для добавления/удаления можно реализовать позже
  return (
    <UserListsContext.Provider value={{
      watchLater, setWatchLater,
      watched, setWatched,
      favorites, setFavorites
    }}>
      {children}
    </UserListsContext.Provider>
  );
} 
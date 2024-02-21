import React, { createContext, useContext, useState, useEffect  } from 'react';

// Setting the app for global variables
const AuthContext = createContext();

// useContext(AuthContext) -> useAuth()
export function useAuth() {
  return useContext(AuthContext);
}

export const AuthProvider = ({ children }) => {
  //Global varable across entire app
  //Resolving refreash bug
  const [loggedIn, setloggedIn] = useState(() => {
    const isUserLoggedIn = localStorage.getItem('loggedIn');
    return isUserLoggedIn === 'true';
  });

  useEffect(() => {
    localStorage.setItem('loggedIn', loggedIn.toString());
  }, [loggedIn])

  //Global Methods
  const login = () => setloggedIn(true);
  const logout = () => {
    setloggedIn(false);
  };

  return (
    /*Any Component within the app will have acess to the global vars and methods*/
    <AuthContext.Provider value={{ loggedIn, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

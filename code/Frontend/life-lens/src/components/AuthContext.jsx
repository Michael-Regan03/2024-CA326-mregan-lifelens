import React, { createContext, useContext, useState } from 'react';

// Setting the app for global variables
const AuthContext = createContext();

// useContext(AuthContext) -> useAuth()
export function useAuth() {
  return useContext(AuthContext);
}

export const AuthProvider = ({ children }) => {
  //Global varable across entire app
  const [loggedIn, setloggedIn] = useState(false);

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

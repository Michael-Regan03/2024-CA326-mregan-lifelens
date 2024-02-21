import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext'; 

export default function Logout() {
  const { logout } = useAuth();
  const nav = useNavigate();

  useEffect(() => {
    //Clear local memory
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');     
    //set loggedIn to false
    logout()
    //Return HomePage
    nav('/')
   
}, [logout, nav]);

  return null
}
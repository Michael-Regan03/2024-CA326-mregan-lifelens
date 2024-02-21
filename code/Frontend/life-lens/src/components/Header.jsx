import React, { useState, useEffect } from 'react';
import loadData from '../loaders/loadData';
import LoggedOutNavbar from './Navbars/LoggedOutNavbar';
import LoggedInNavbar from './Navbars/LoggedInNavbar';
import '../style_components/Header.css'
import {useAuth} from '../context/AuthContext'


function Header() {
  const [name, setName] = useState([]);
  const { loggedIn } = useAuth();

  useEffect(() => {
    if (loggedIn) {
      const fetchUserInfo = async () => {
        try {
          const response = await loadData('http://127.0.0.1:8000/current_user/', 'GET');
          if (response && response.name) {
            setName(response.name);
          } else {
            console.log("User not logged in or account no longer exists");
          }
        } catch (error) {
          console.error(error);
        }
      };
      fetchUserInfo();
    }}, [loggedIn]);

if(loggedIn){
  return(
    <div>
        <h1>Welcome to lifelens, {name} </h1>
        <LoggedInNavbar></LoggedInNavbar>
    </div>
  );
}else{
  return(
    <div>
        <h1>Welcome to lifelens</h1>
        <LoggedOutNavbar></LoggedOutNavbar>
    </div>
  );
}

}

export default Header;
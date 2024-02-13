import React, { useState, useEffect } from 'react';
import loadData from '../loaders/loadData';
import DaysDropDownMenu from './DaysDropDownMenu';

function Header() {
  const [userData, setUserData] = useState([]);
  const accessToken = localStorage.getItem('accessToken'); 
  
  useEffect( () => {
    if (accessToken) {
    const fetchUserInfo = async () => {try{
      const responce = await loadData('http://127.0.0.1:8000/current_user/','GET')
      setUserData(responce)
      }catch(error){
          console.error(error)
        }
  }
  fetchUserInfo()
}}, []); //load only on refreash

if(!accessToken){
  return(
    <div>
        <h1>Welcome to lifelens</h1>
    </div>
  );
}

return(
  <div>
    <h1>Welcome to lifelens, {userData.name} </h1>
    <DaysDropDownMenu></DaysDropDownMenu>
  </div>
);


}

export default Header;
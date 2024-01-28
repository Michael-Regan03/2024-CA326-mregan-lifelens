import React, { useState, useEffect } from 'react';

function Homepage() {
  const [userData, setUserData] = useState([]);
  const accessToken = localStorage.getItem('accessToken'); 

  useEffect(() => {
    if (!accessToken) {
      
      return(
      <div>
      <h1>Life-Lens</h1>
      </div>
  )}

    fetch('http://127.0.0.1:8000/current_user/', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${accessToken}`, 
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        if (response.status === 401) {
          throw new Error('Unauthorized');
        }
        return response.json();
      })
      .then((data) => {
        setUserData(data);
      })
      .catch((error) => {
        console.error('Error:', error.message);
      });
  }, [accessToken]);

  return (
    <div>
      <h1> Welcome back to Life-Lens {userData.name} </h1>
    </div>
  );
}

export default Homepage;
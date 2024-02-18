import React, { useState } from 'react';
import FetchComp from '../actions/FetchComp';
import { useNavigate } from 'react-router-dom';
import Header from '../components/Header';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const nav = useNavigate();

  const submitForm = async (e) => {
    e.preventDefault();
    try {
      const response = await FetchComp("http://127.0.0.1:8000/auth/jwt/create/?Content-type=application/json", { email , password }, 'POST');
      console.log('Login successful:', response);
      //storing access and refreash tokens locally
      localStorage.setItem('accessToken', response.access);
      localStorage.setItem('refreshToken', response.refresh);
      //redirect to homepage
      nav('/');
    } catch (error) {  
      console.error('Login failed:', error);
      
    }
  };

  return(
    
    <div className="login-wrapper">
      <Header></Header>
      <h2 className="form-header">Please Log In</h2>
      <form onSubmit={submitForm}>
        <label>
          <p>Email</p>
          <input type="text" onChange={(e) => setEmail(e.target.value)} />
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={(e) => setPassword(e.target.value)} />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    
    </div>
  )
}
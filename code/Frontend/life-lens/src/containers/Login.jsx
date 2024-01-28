import React, { useState } from 'react';
import handleSubmit from '../actions/handleSubmit';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const nav = useNavigate();

  const submitForm = async (e) => {
    e.preventDefault();
    try {
      const response = await handleSubmit("http://127.0.0.1:8000/auth/jwt/create/?Content-type=application/json", { email , password });
      console.log('Login successful:', response);
      localStorage.setItem('accessToken', response.accessToken);
      localStorage.setItem('refreshToken', response.refreshToken);
      nav('/');
    } catch (error) {
      console.error('Login failed:', error);
      
    }
  };

  return(
    <div className="login-wrapper">
      <h1>Please Log In</h1>
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
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import handleSubmit from '../actions/handleSubmit';

export default function Signup() {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [re_password, setRePassword] = useState('');
  const nav = useNavigate(); 

    const submitForm = async (e) => {
    e.preventDefault();
    try {
      const response = await handleSubmit("http://127.0.0.1:8000/auth/users/?Content-Type=application/json", { email,name, password, re_password });
      console.log('Login successful:', response);
      nav('/AwaitEmail');
    } catch (error) {
      console.error('Login failed:', error);
      
    }
  };   


  return(
    <div className="Signup-wrapper">
      <h1>Sign up</h1>
      <form onSubmit={submitForm}>
        <label>
          <p>Email</p>
          <input type="text" onChange={(e) => setEmail(e.target.value)} />
        </label>
        <label>
          <p>name</p>
          <input type="text" onChange={(e) => setName(e.target.value)} />
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={(e) => setPassword(e.target.value)} />
        </label>
        <label>
          <p>Password Verification</p>
          <input type="password" onChange={(e) => setRePassword(e.target.value)} />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
      

    </div>
  )
  }
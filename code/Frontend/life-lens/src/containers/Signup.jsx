import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FetchComp from '../actions/FetchComp';
import renderSelectOptions from '../actions/renderSelectOptions';
import '../style_components/FormVerification.css'

export default function Signup() {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');

  const [re_password, setRePassword] = useState('');


  const [loadError, setLoadError] = useState(false);
  const [error, setError] = useState(null);
  const nav = useNavigate();



  const genders = { 0: "Male",
                    1: "Female"}

  const submitForm = async (e) => {
    e.preventDefault();
    try {
      const body = {
        "email" : email,
        "name": name,
        "password": password,
        "re_password": re_password,
        "age": age,
        "gender": gender,
      }

      const response = await FetchComp('http://127.0.0.1:8000/auth/users/?Content-Type=application/json', body, 'POST');
      console.log('Login successful:', response);
        
      nav('/login');

    } catch (error) {
      console.error('Login failed:', error);

      console.log(error)
      setLoadError(true)
      setError("Failed to Create Account")
      
    }
  };   


  return(
    <div>
      <h2 className="form-header" >Sign up</h2>
      <form onSubmit={submitForm}>
        <label>
          <p>Email</p>
          <input type={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <label>
          <p>name</p>
          <input type={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <label>
          <p>Age</p>
          <input type={age} onChange={(e) => setAge(e.target.value)} />
        </label>
      
        <div>
          <p>Gender</p>
          <select value={gender} onChange={(e) => { if(e.target.value !== "Select"){ setGender(e.target.value)}else{ setGender('')}}}>
            <option>Select </option>
            {renderSelectOptions(genders)}
          </select>
        </div>

        <label>
          <p>Password</p>
          <input type="password"  onChange={(e) => setPassword(e.target.value)} />
        </label>
        <label>
          <p>Password Verification</p>
          <input type="password" onChange={(e) => setRePassword(e.target.value)} />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>

      {loadError && <p className="error-message">{error}</p>}

    </div>
  )
  }
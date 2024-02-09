import React from 'react';
import { useState } from 'react';
import logo from './logo.svg';
import './App.css';

import DailyActivityForm from'./components/DailyActivityForm';

import Home from './containers/Home'
import Login from './containers/Login'
import Signup from './containers/Signup'
import Activate from './containers/Activate'
import ResetPassword from './containers/ResetPassword'
import ResetPasswordConfirm from './containers/ResetPasswordConfirm'
import AwaitEmail from './containers/AwaitEmail'

import { BrowserRouter, Route, Switch, Routes } from 'react-router-dom';

import Layout from './hocs/Layout';





function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/"element={<Home />} />

        <Route path="/signup" element={<Signup />} />
        <Route path="/awaitemail" element={<AwaitEmail />} />

        <Route path="/login" element={<Login />} />



        <Route path="/upload" element={<DailyActivityForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

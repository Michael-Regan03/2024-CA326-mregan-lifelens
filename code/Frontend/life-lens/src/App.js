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
import ChronicIllnessRiskAssesment from './components/ChronicIllnessRiskAssesment'
import { BrowserRouter, Route, Switch, Routes } from 'react-router-dom';

import SurveyForm from './components/SurveyForm';

import Visualisations from './containers/Visualisations';

import Header from './components/Header';


function App() {
  return(
    <BrowserRouter>
      <Header></Header>
      <Routes>
        <Route path="/"element={<Home />} />

        <Route path="/signup" element={<Signup />} />
        <Route path="/awaitemail" element={<AwaitEmail />} />

        <Route path="/login" element={<Login />} />

        <Route path="/risk-assesment" element={<ChronicIllnessRiskAssesment />} />
        <Route path="/survey" element={<SurveyForm />} />
        <Route path="/upload" element={<DailyActivityForm />} />
        <Route  path="/Visualisations" element={<Visualisations />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

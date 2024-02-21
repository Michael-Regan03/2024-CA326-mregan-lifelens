import React from 'react';
import { useState } from 'react';
import './App.css';

import DailyActivityForm from'./components/forms/DailyActivityForm';

import Home from './containers/Home'
import Login from './containers/Login'
import Signup from './containers/Signup'
import ChronicIllnessRiskAssesment from './components/ChronicIllnessRiskAssesment'
import { BrowserRouter, Route,  Routes } from 'react-router-dom';

import SurveyForm from './components/forms/SurveyForm';

import Visualisations from './containers/Visualisations';

import Header from './components/Header';

import Logout from './containers/Logout';
import { AuthProvider } from './context/AuthContext';


function App() {
  return(
    <AuthProvider>
      <BrowserRouter>
        <Header></Header>
        <Routes>
          <Route path="/"element={<Home />} />

          <Route path="/signup" element={<Signup />} />

          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/signup" element={<Signup />} />

          <Route path="/risk-assesment" element={<ChronicIllnessRiskAssesment />} />
          <Route path="/survey" element={<SurveyForm />} />
          <Route path="/upload" element={<DailyActivityForm />} />
          <Route  path="/Visualisations" element={<Visualisations />}/>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;

import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import PieChart from './PieChart';
import AddItemOrUpdateDuration from '../actions/AddItemOrUpdateDuration';
import '../style_components/Navbar.css'

const LoggedInNavbar = () => (
    <div className="navbar" >
        <a href="http://localhost:3000/upload" >Upload LifeLog Data</a>
        <a href="http://localhost:3000/survey">Fill out Survey</a>
        <a href="http://localhost:3000/visualisations" >Visualise Data</a>
        <a href="http://localhost:3000/risk-assesment">Chronic Illness Risk Assessment</a>
        <a>Sign out</a>
    </div>
);

export default LoggedInNavbar;
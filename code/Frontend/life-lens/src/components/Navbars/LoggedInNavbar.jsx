import React from 'react';
import '../../style_components/Navbar.css'
import { Link } from 'react-router-dom';

const LoggedInNavbar = () => (
    <div className="navbar" >
        <Link to="/" >Home Page</Link>
        <Link to="/upload" >Upload LifeLog Data</Link>
        <Link to="/survey">Fill out Survey</Link>
        <Link to="/visualisations" >Visualise Data</Link>
        <Link to="/risk-assesment">Chronic Illness Risk Assessment</Link>
        <Link to="/logout ">Sign out</Link>
    </div>
);

export default LoggedInNavbar;
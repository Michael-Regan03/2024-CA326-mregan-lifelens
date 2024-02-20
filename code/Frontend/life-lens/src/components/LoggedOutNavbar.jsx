import React from 'react';
import '../style_components/Navbar.css'
import { Link } from 'react-router-dom';

const LoggedOutNavbar = () => (
    <div className="navbar">
        <Link  to="/signup ">Create an accont</Link>
        <Link  to="/login ">Sign in</Link>
    </div>
);

export default LoggedOutNavbar;
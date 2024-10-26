import React from 'react';
import './Header.css';
import logo from '../assets/nergy_vidya_logo.svg';

const Header = () => {
    return (
        <header className="header">
            <img src={logo} alt="Nergy Vidya" className="logo" />
            <nav className="nav-bar">
                <ul>
                    <li>Dashboard</li>
                    <li>Services</li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
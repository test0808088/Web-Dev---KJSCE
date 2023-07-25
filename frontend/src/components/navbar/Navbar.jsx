import React from 'react';
import './navbar.css';
import {FaBars, FaRegUser} from 'react-icons/fa'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser,faBars } from '@fortawesome/free-solid-svg-icons';
import { useState,useRef } from 'react';

const Navbar = ({ showAchievementsButton }) => {
    const [menuOpen,setMenuOpen]=useState(false)
  return (
    <nav className="navbar">
      <div className="logo">
        <img src="https://lms-kjsce.somaiya.edu/pluginfile.php/1/theme_essential/logo/1687177320/engg-logo.png" alt="Logo" className="logoImage" />
      </div>
    
      {/* <div className={`mobileMenuIcon ${showMobileMenu ? 'open' : ''}`} onClick={toggleMobileMenu}>
        <FontAwesomeIcon icon={faBars} />
      </div> */}
      {/* Navigation links */}

      <div className='menu' onClick={()=>{
        setMenuOpen(!menuOpen)
      }}>
        <FaBars/>

      </div>
      <ul className= {menuOpen?"open":"navLinks"}>
      {showAchievementsButton &&<li className="navItem achievementsButton">Achievements</li>}
        <li className="navItem profileButton"><FontAwesomeIcon className="user-icon" icon={faUser} />My Profile</li>
        <li className="navItem logoutLink">Logout</li>
      </ul>
    </nav>
  );
};



export default Navbar;

import React from 'react';
import './Footer.css'; // Create a CSS file named "Footer.css" for styling
import { FaInstagram, FaFacebook, FaLinkedin, FaTwitter } from 'react-icons/fa';



const Footer = () => {
  return (
    <footer className="footer">
      <div className="column">
        <img src="https://uploads.sarvgyan.com/2021/04/KJ-Somaiya-College-of-Engineering.png" alt="Logo" className="logoImage" />
      </div>
      <div className="column">
        <h4>Student Help</h4>
        <p>International Tieups</p>
        <p>Scholarships</p>
        <p>Alumni Portal</p>
      </div>
      <div className="column">
        <h4>Get in Touch</h4>
        <p>Maps & Directions</p>
        <p>Contact Directory</p>
        <p>Faculty Directory</p>
        <p>Emergency</p>
        <p>Events & Updates</p>
        <p>Gallery</p>
      </div>
      <div className="column followUsOnColumn">
        <h4>Follow us on</h4>
        <p className="instagram"><FaInstagram /></p>
        <p><FaFacebook/></p>
        <p><FaTwitter/></p>
        <p><FaLinkedin/></p>
      </div>
    </footer>
  );
};

export default Footer;

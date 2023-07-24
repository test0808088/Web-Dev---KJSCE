import React from 'react';
import { FaUser } from 'react-icons/fa';
import "./profile.css"
import { useState,useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
    const [userData, setUserData] = useState(null);
    useEffect(() => {
        const fetchUserData = async () => {
          try {
            const response = await axios.get('http://127.0.0.1:8000/student/'); 
            // console.log(response.data)
            const Data = response.data.find(
              (user) => user.id === 3
            );
            setUserData(Data);
          } catch (error) {
            console.error('Error fetching data:', error);
          }
        };
    
        fetchUserData();
      }, []);   

  return (
    <div className="profile-container">
      {userData ? (
        <div className="profile-subcontainer">
          <div className="user-section">
            <div className="user-icon">
              <FaUser size={126} color="#941919" />
            </div>
            <div className="vertical-line"></div>
            <div className="user-details">
              <h2>{userData.student_name}</h2>
              <p>Roll Number: {userData.Roll_number}</p>
              <p>Email: {userData.email}</p>
              <p>Student Contact No: {userData.Student_contact_no}</p>
              <p>Parents Contact No: {userData.Parents_contact_no}</p>
              <p>Parent Email ID: {userData.Parent_email_id}</p>
              <p>Branch: {userData.student_branch.branch_name}</p>
              
            </div>
          </div>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Profile;

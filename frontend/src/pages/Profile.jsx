import React from "react";
import Navbar from "../components/navbar/Navbar";
import Footer from "../components/footer/Footer";
import Profile from "../components/studentProfile/Profile";


function ProfilePage(){
    return(
        <>
            <Navbar showAchievementsButton={true}/>
            <Profile/>
            <Footer/>
        </>
    )
}

export default ProfilePage
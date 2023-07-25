import React from "react";
import Navbar from "../components/navbar/Navbar";
import Footer from "../components/footer/Footer";

function FacultyPage(){
    return(
        <>
            <Navbar showAchievementsButton={false}/>
            Faculty
            <Footer/>
        </>
    )
}

export default FacultyPage
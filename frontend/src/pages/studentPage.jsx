import React from "react";
import Navbar from "../components/navbar/Navbar";
import Footer from "../components/footer/Footer";
import Records from "../components/studentRecords/Records";
function StudentPage(){
    return(
        <>
            <Navbar showAchievementsButton={true}/>
            <Records/>
            <Footer/>
        </>
    )
}

export default StudentPage  
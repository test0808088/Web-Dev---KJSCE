import React from "react"
import StudentPage from "./pages/studentPage"
import AchievementsPage from "./pages/achievementsPage";
import ProfilePage from "./pages/Profile";
import FacultyPage from "./pages/facultyPage";
import { BrowserRouter,Route,Routes } from "react-router-dom";



function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/student" element={<StudentPage/>} />
          <Route path="/achievement" element={<AchievementsPage/>}/>
          <Route path="/profile" element={<ProfilePage/>}/>
          <Route path="/faculty" element={<FacultyPage/>}/>
        </Routes>
      </BrowserRouter>
      
    </>
  )
}

export default App

import React from "react"
import StudentPage from "./pages/studentPage"
import AchievementsPage from "./pages/achievementsPage";
import ProfilePage from "./pages/Profile";
import { BrowserRouter,Route,Routes } from "react-router-dom";



function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/student" element={<StudentPage/>} />
          <Route path="/achievement" element={<AchievementsPage/>}/>
          <Route path="/profile" element={<ProfilePage/>}/>

        </Routes>
      </BrowserRouter>
      
    </>
  )
}

export default App

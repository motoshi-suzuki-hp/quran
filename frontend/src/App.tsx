import React from "react";
import Home from "./pages/Home";
import List from "./pages/List";
import Detail from "./pages/Detail";
import Sidebar from "./Sidebar";
import Header from "./Header";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Profile from "./pages/Profile";  // 任意
import PrivateRoute from "./pages/PrivateRoute"; 
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";

const App: React.FC = () => {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <div className="main-content">
          <Sidebar />
          <div className="content">
            <Routes>
              {/* 既存 */}
              <Route path="/" element={ <div><Home /></div> } />
              
              {/* Profile を保護したい場合は PrivateRoute でラップ */}
              <Route
                path="/profile"
                element={
                  <PrivateRoute>
                    <Profile />
                  </PrivateRoute>
                }
              />
              <Route 
                path="/:surah_id" 
                element={ 
                  <PrivateRoute>
                    <List />
                  </PrivateRoute> 
                }
              />
              <Route 
                path="/:surah_id/:ayah_id" 
                element={ 
                  <PrivateRoute>
                    <Detail />
                  </PrivateRoute> 
                }
              />

              {/* 追加: 認証系 */}
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Signup />} />
              <Route path="/profile" element={<Profile />} /> {/* 任意 */}
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
};

export default App;

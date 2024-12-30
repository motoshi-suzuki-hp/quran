import React from "react";
// import "./reset.css";
import Home from "./pages/Home";
import List from "./pages/List";
import Detail from "./pages/Detail";
import Sidebar from "./Sidebar";
import Header from "./Header";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";

const App: React.FC = () => {
  return (
    <Router>
      <div className="app-container">
        <Header />
          <div className="content">
            <Routes>
              <Route path="/" element={<div><Home /></div>} />
              <Route path="/:surah_id" element={
                <div className="main-content">
                  <Sidebar />
                  <div><List /></div>
                </div>
              } />
              <Route path="/:surah_id/:ayah_id" element={
                <div className="main-content">
                  <Sidebar />
                  <div><Detail /></div>
                </div>
              } />
              {/* ここに他のルートを追加 */}
            </Routes>
        </div>
      </div>
    </Router>
  );
};
export default App;

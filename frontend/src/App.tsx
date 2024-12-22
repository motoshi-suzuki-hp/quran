import React from "react";
// import "./reset.css";
import List from "./List";
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
        <div className="main-content">
          <Sidebar />
          <div className="content">
            <Routes>
              <Route path="/" element={<div><List /></div>} />
              <Route path="/:surah_id" element={<div><List /></div>} />
              <Route path="/:surah_id/:ayah_id" element={<div><Detail /></div>} />
              {/* ここに他のルートを追加 */}
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
};
export default App;

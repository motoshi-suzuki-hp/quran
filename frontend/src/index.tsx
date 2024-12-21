import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import App from '/app/src/App';
import Detail from '/app/src/pages/Detail';
import '/app/src/App.css';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/:id" element={<Detail />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

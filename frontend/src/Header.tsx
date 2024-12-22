import React from 'react';
import "./header.css";
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="header">
      <h1>
        <Link to="/">Quran.ai</Link>
      </h1>
    </header>
  );
};

export default Header;

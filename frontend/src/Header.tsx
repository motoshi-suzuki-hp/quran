import React from 'react';
import LogoutButton from "./LogoutButton"
import ProfileButton from "./ProfileButton"
import "./header.css";
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="header">
      <h1>
        <Link to="/">Quran.ai</Link>
      </h1>
      <div>
        <LogoutButton />
        <ProfileButton />
      </div>
    </header>
  );
};

export default Header;

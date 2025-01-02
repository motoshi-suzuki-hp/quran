import React from 'react';
import { Link } from 'react-router-dom';
import { Surahs, NumberOfSurahs} from './const';
import "./sidebar.css";

const Sidebar: React.FC = () => {
  return (
    <div className="sidebar">
        <ul>
            {Array.from({ length: NumberOfSurahs }, (_, index) => (
                <li key={index}>
                    <Link to={`/${index + 1}`}>{index+1}. {Surahs[index]}</Link>
                </li>
            ))}
        </ul>
    </div>
  );
};

export default Sidebar;

import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Surahs, NumberOfSurahs } from './const';
import "./sidebar.css";

const Sidebar: React.FC = () => {
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);
  const navigate = useNavigate();

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth <= 768);
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const surahId = e.target.value;
    if (surahId !== "") {
      navigate(`/${surahId}`);
    }
  };

  if (isMobile) {
    // スマホ向け: select, optionを使用
    return (
      <div className="sidebar-mobile">
        <select onChange={handleSelectChange} defaultValue="">
          <option value="">選択してください</option>
          {Array.from({ length: NumberOfSurahs }, (_, index) => (
            <option key={index} value={index + 1}>
              {index + 1}. {Surahs[index]}
            </option>
          ))}
        </select>
      </div>
    );
  }

  // PC向け: 従来のサイドバー
  return (
    <div className="sidebar">
      <ul>
        {Array.from({ length: NumberOfSurahs }, (_, index) => (
          <li key={index}>
            <Link to={`/${index + 1}`}>{index + 1}. {Surahs[index]}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;

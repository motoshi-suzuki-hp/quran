// frontend/src/ProfileButton.tsx
import React from "react";
import { useNavigate } from "react-router-dom";

const ProfileButton: React.FC = () => {
  const navigate = useNavigate();

  const token = sessionStorage.getItem("access_token");

  const handleProfile = () => {
    navigate("/profile");
  };

  if (token) {
    return (
        <button onClick={handleProfile}>
          Profile
        </button>
    );
  };
};

export default ProfileButton;

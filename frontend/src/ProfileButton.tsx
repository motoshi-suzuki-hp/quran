// frontend/src/ProfileButton.tsx
import React from "react";
import { useNavigate } from "react-router-dom";

const ProfileButton: React.FC = () => {
  const navigate = useNavigate();

  const handleProfile = () => {
    navigate("/profile");
  };

  return (
      <button onClick={handleProfile}>
        Profile
      </button>
  );
};

export default ProfileButton;

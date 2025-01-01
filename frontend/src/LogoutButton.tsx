// frontend/src/LogoutButton.tsx
import React from "react";
import { useNavigate } from "react-router-dom";

const LogoutButton: React.FC = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    // ログアウト処理: ローカルストレージからトークン等を削除
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");
    // ログインページへリダイレクト
    navigate("/login");
  };

  return (
      <button onClick={handleLogout}>
        ログアウト
      </button>
  );
};

export default LogoutButton;

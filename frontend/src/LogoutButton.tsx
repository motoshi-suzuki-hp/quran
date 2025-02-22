// frontend/src/LogoutButton.tsx
import React from "react";
import { useNavigate } from "react-router-dom";

const LogoutButton: React.FC = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    // ログアウト処理: ローカルストレージからトークン等を削除
    sessionStorage.removeItem("access_token");
    sessionStorage.removeItem("refresh_token");
    sessionStorage.removeItem("user");
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

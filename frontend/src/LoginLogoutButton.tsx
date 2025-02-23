// frontend/src/LoginLogoutButton.tsx
import React from "react";
import { useNavigate } from "react-router-dom";

const LoginLogoutButton: React.FC = () => {
  const navigate = useNavigate();

  const token = sessionStorage.getItem("access_token");
  
  const handleLogout = () => {
    // ログアウト処理: ローカルストレージからトークン等を削除
    sessionStorage.removeItem("access_token");
    sessionStorage.removeItem("refresh_token");
    sessionStorage.removeItem("user");
    // ログインページへリダイレクト
    navigate("/login");
  };
  const handleLogin = () => {
    // ログインページへリダイレクト
    navigate("/login");
  };

  if (token) {
    return (
        <button onClick={handleLogout}>
          ログアウト
        </button>
    );
  } else {
    return (
      <button onClick={handleLogin}>
        ログイン
      </button>
  );
  }
};

export default LoginLogoutButton;

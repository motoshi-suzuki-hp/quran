import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AUTH_API_URL } from '../const';

const Profile: React.FC = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchUser = async () => {
      const token = sessionStorage.getItem("access_token");
      if (!token) {
        setError("トークンがありません。ログインしてください。");
        return;
      }
      try {
        const response = await fetch(`${AUTH_API_URL}/me`, {
          method: "GET",
          headers: {
            "Authorization": `Bearer ${token}`
          }
        });
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || "ユーザー情報の取得に失敗しました");
        }
        const result = await response.json();
        setUser(result);
      } catch (err: any) {
        console.error(err);
        setError(err.message || "ユーザー情報の取得に失敗しました");
      }
    };
    fetchUser();
  }, []);

  const handleProfile = () => {
    sessionStorage.removeItem("access_token");
    sessionStorage.removeItem("refresh_token");
    sessionStorage.removeItem("user");
    navigate("/login");
  };

  if (error) {
    return (
      <div style={{ padding: "20px" }}>
        <h1>マイページ</h1>
        <p style={{ color: "red" }}>{error}</p>
        <button onClick={() => navigate("/login")}>ログインページへ</button>
      </div>
    );
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>マイページ</h1>
      {user ? (
        <div>
          <p><strong>ID:</strong> {user.id}</p>
          <p><strong>Username:</strong> {user.username}</p>
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>Role:</strong> {user.role}</p>
        </div>
      ) : (
        <p>読み込み中...</p>
      )}
      
      <button onClick={handleProfile} style={{ marginTop: "20px" }}>
        ログアウト
      </button>
    </div>
  );
};

export default Profile;

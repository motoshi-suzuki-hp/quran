import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Signup: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  // パスワード確認用に2つのStateを持ちます
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [error, setError] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSuccessMessage("");

    if (password !== confirmPassword) {
      setError("パスワードが一致しません。");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5001/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
          username,
          email,
          password 
        })
      });

      if (!response.ok) {
        // 400, 500 など
        const errorData = await response.json();
        throw new Error(errorData.error || "Sign up failed");
      }

      const result = await response.json();
      console.log("Signup result:", result);

      setSuccessMessage("ユーザー登録が完了しました。ログインしてください。");
        navigate(`/login`);
    } catch (err: any) {
      console.error(err);
      setError(err.message || "ユーザー登録に失敗しました");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>新規登録</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}

      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "300px" }}>
        <label htmlFor="username">ユーザー名</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <label htmlFor="email">メールアドレス</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label htmlFor="password">パスワード</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <label htmlFor="confirmPassword">パスワード(確認)</label>
        <input
          type="password"
          id="confirmPassword"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />

        <button type="submit" style={{ marginTop: "20px" }}>登録</button>
      </form>

      <p style={{ marginTop: "10px" }}>
        すでにアカウントをお持ちですか？{" "}
        <span
          style={{ color: "blue", textDecoration: "underline", cursor: "pointer" }}
          onClick={() => navigate("/login")}
        >
          ログインはこちら
        </span>
      </p>
    </div>
  );
};

export default Signup;

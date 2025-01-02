import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login: React.FC = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:5001/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      console.log("email:", email);
      console.log("password:", password);

      if (!response.ok) {
        // 401や500など
        const errorData = await response.json();
        throw new Error(errorData.error || "Login failed");
      }

      const result = await response.json();
      console.log("Login result:", result);

      // アクセストークンとリフレッシュトークンをローカルストレージに保存
      localStorage.setItem("access_token", result.access_token);
      localStorage.setItem("refresh_token", result.refresh_token);

      // 必要ならユーザー情報も保存
      localStorage.setItem("user", JSON.stringify(result.user));

      // ログイン成功後、トップページやプロフィールページへ遷移
      navigate("/");
    } catch (err: any) {
      console.error(err);
      setError(err.message || "ログインに失敗しました");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>ログイン</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "300px" }}>
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

        <button type="submit" style={{ marginTop: "20px" }}>ログイン</button>
      </form>

      <p style={{ marginTop: "10px" }}>
        アカウントをお持ちでないですか？{" "}
        <span
          style={{ color: "blue", textDecoration: "underline", cursor: "pointer" }}
          onClick={() => navigate("/signup")}
        >
          新規登録はこちら
        </span>
      </p>
    </div>
  );
};

export default Login;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AUTH_API_URL } from '../const';
import { LANGUAGE } from '../const';

const Signup: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  // パスワード確認用に2つのStateを持ちます
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  // ドロップダウン用のState
  const [firstLanguage, setFirstLanguage] = useState("");
  const [secondLanguage, setSecondLanguage] = useState("");
  const [thirdLanguage, setThirdLanguage] = useState("");

  const [error, setError] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSuccessMessage("");

    // パスワード一致確認
    if (password !== confirmPassword) {
      setError("パスワードが一致しません。");
      return;
    }

    // 第一言語は必須チェック
    if (!firstLanguage) {
      setError("第一言語は必須です。");
      return;
    }

    // 重複チェック（空文字は除外）
    const selectedLanguages = [firstLanguage, secondLanguage, thirdLanguage].filter(lang => lang !== "");
    const uniqueCount = new Set(selectedLanguages).size;
    if (uniqueCount !== selectedLanguages.length) {
      setError("第一言語、第二言語、第三言語はすべて異なるものを選択してください。");
      return;
    }

    try {
      const response = await fetch(`${AUTH_API_URL}/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
          username,
          email,
          password,
          first_language: firstLanguage,
          second_language: secondLanguage,
          third_language: thirdLanguage
        })
      });

      if (!response.ok) {
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

        {/* 第一言語（必須）のドロップダウン */}
        <label htmlFor="firstLanguage">第一言語 <span style={{ color: "red" }}>*</span></label>
        <select
          id="firstLanguage"
          value={firstLanguage}
          onChange={(e) => setFirstLanguage(e.target.value)}
          required
        >
          {LANGUAGE.map(option => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>

        {/* 第二言語 */}
        <label htmlFor="secondLanguage">第二言語</label>
        <select
          id="secondLanguage"
          value={secondLanguage}
          onChange={(e) => setSecondLanguage(e.target.value)}
        >
          {LANGUAGE.map(option => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>

        {/* 第三言語 */}
        <label htmlFor="thirdLanguage">第三言語</label>
        <select
          id="thirdLanguage"
          value={thirdLanguage}
          onChange={(e) => setThirdLanguage(e.target.value)}
        >
          {LANGUAGE.map(option => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>

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

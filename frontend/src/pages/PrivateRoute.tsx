import React from "react";
import { Navigate, useLocation } from "react-router-dom";

type PrivateRouteProps = {
  children: JSX.Element;
};

const PrivateRoute: React.FC<PrivateRouteProps> = ({ children }) => {
  const location = useLocation();

  // ローカルストレージにあるトークンをチェック
  const accessToken = localStorage.getItem("access_token");

  // もしトークンが無い or 空文字なら、ログインページへリダイレクト
  if (!accessToken) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }

  // トークンが存在するので、そのままchildrenを表示
  return children;
};

export default PrivateRoute;

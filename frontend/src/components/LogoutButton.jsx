import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../contexts/UserContext"; // Adjust the import path as needed

const LogoutButton = () => {
  const navigate = useNavigate();
  const { logout } = useContext(UserContext);

  const handleLogout = () => {
    logout();
    navigate("/login"); // Navigate to login page after logout
  };

  return <button onClick={handleLogout}>Logout</button>;
};

export default LogoutButton;

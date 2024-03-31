import React, { useContext } from "react";
import UserContext from "../contexts/UserContext"; // Adjust the import path as needed

const ErrorMessage = () => {
  const { error } = useContext(UserContext);

  if (!error) return null; // Don't render anything if there's no error

  return <div style={{ color: "red", marginBottom: "10px" }}>{error}</div>;
};

export default ErrorMessage;

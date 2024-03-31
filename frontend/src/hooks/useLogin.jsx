import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { message } from "antd";
import { UserContext } from "../contexts/UserContext";

const useLogin = () => {
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(null);
  const [, setToken] = useContext(UserContext);
  const navigate = useNavigate();

  const loginUser = async (values) => {
    try {
      setError(null);
      setLoading(true);

      // Format the data as URL-encoded form data
      const formData = new URLSearchParams();
      formData.append("username", values.email);
      formData.append("password", values.password);

      const res = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData,
      });

      const data = await res.json();

      if (res.status === 200) {
        message.success("User logged in successfully!");
        setToken(data.access_token);
        navigate("/dashboard");
      } else if (res.status === 403) {
        setError(data.detail);
      } else {
        message.error("Login failed");
      }
    } catch (error) {
      message.error("Login failed");
    } finally {
      setLoading(false);
    }
  };

  return { loading, error, loginUser };
};

export default useLogin;

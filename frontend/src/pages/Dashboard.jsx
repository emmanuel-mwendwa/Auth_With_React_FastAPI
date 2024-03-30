import React, { useContext, useEffect, useState } from "react";
import { UserContext } from "../contexts/UserContext";
import {
  Button,
  message,
  Card,
  Flex,
  Alert,
  Spin,
  Typography,
  Form,
} from "antd";

const Dashboard = () => {
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(null);
  const [profile, setProfile] = useState(null);
  const [token, setToken] = useContext(UserContext);

  const getUserProfile = async () => {
    try {
      setError(null);
      setLoading(true);
      const res = await fetch("http://localhost:8000/users/me", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();

      if (res.status === 200) {
        setProfile(data);
      } else if (res.status === 401) {
        setError(data.detail);
      } else {
        message.error("Something went wrong");
      }
    } catch (error) {
      message.error("Registration failed");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getUserProfile();
  }, []);

  const handleLogout = () => {
    setToken(null);
  };

  return (
    <>
      <Card className="form-container">
        <Flex gap="large" align="center">
          <Flex vertical flex={1}>
            <Typography.Title level={3} strong className="title">
              Profile
            </Typography.Title>
            {token && profile ? (
              <>
                {error && (
                  <Alert
                    description={error}
                    type="error"
                    showIcon
                    closable
                    className="alert"
                  />
                )}
                <Form.Item label="First Name">
                  <div>{profile.firstname}</div>
                </Form.Item>
                <Form.Item label="Last Name">
                  <div>{profile.lastname}</div>
                </Form.Item>
                <Form.Item label="Email">
                  <div>{profile.email}</div>
                </Form.Item>
              </>
            ) : (
              { loading }
            )}
          </Flex>
        </Flex>
      </Card>
      <div>Profile</div>

      {token && <Button onClick={handleLogout}>Logout</Button>}
    </>
  );
};

export default Dashboard;

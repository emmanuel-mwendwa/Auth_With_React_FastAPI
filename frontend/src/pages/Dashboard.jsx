import React, { useEffect, useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { Button } from "antd";

const Dashboard = () => {
  const { logout } = useAuth();
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const userId = 4;
      const tokenData = localStorage.getItem("user_data");
      const token = tokenData.getItem("userToken");

      try {
        const response = await fetch(`http://localhost:8000/users/${userId}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("Could not fetch user data");
        }

        const data = await response.json();
        setUser(data);
      } catch (error) {
        console.error("Error fetching user:", error);
      }
    };

    fetchData();
  }, []);

  if (!user) {
    return (
      <>
        <div>Loading...</div>;<Button onClick={logout}>Logout</Button>
      </>
    );
  }

  return (
    <>
      <div>Profile</div>
      <div>
        {user.firstname} - {user.lastname}
      </div>
      <div>{user.email}</div>
      <Button onClick={logout}>Logout</Button>
    </>
  );
};

export default Dashboard;

import React, { createContext, useEffect, useState } from "react";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("awesomeLeadsToken"));

  useEffect(() => {
    const fetchUser = async () => {
      if (!token) return;

      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
      };

      try {
        const response = await fetch("/users/me", requestOptions);

        if (!response.ok) {
          return;
        }
      } catch (error) {
        console.error("Error fetching user: ", error);
      }
    };

    fetchUser();
  }, [token]);

  // Update the token in local storage whenever it changes
  useEffect(() => {
    if (token) {
      localStorage.setItem("awesomeLeadsToken", token);
    } else {
      localStorage.removeItem("awesomeLeadsToken");
    }
  }, [token]);

  // Logout function
  const logout = () => {
    setToken(null);
  };

  return (
    <UserContext.Provider value={{ token, setToken, logout }}>
      {children}
    </UserContext.Provider>
  );
};

import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const getUser = async (id) => {
  const response = await api.get(`/users/${id}`, {
    timeout: 10 * 100,
  });

  if (response.status === 400 || response.status === 500) {
    throw response.data;
  }

  return response.data;
};

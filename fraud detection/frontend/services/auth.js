import axios from 'axios';

const API_URL = 'http://localhost:5000/api/auth';

export const login = async (email, password) => {
  const response = await axios.post(`${API_URL}/login`, { email, password });
  localStorage.setItem('user', JSON.stringify(response.data));
  return response.data;
};

export const register = async (email, password, name) => {
  const response = await axios.post(`${API_URL}/register`, { email, password, name });
  localStorage.setItem('user', JSON.stringify(response.data));
  return response.data;
};

export const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem('user'));
};

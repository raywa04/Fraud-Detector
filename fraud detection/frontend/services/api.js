import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const getTweets = async (keyword) => {
  const response = await axios.get(`${API_URL}/api/tweets?keyword=${keyword}`);
  return response.data;
};

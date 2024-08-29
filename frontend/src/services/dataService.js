// services/dataService.js

import axios from 'axios';

export const getData = async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/items');
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

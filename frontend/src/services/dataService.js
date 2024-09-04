import axios from 'axios';


export const getAllData = async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/all');
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export const getProfitData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/lucros/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

export const getRevenueData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export const getExpensesData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/${month}`);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}
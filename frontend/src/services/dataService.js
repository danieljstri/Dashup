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

export const getRevenueExamsData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/exames/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export const getRevenueAnesthesiaData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/anestesia/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export const getRevenueCashData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/dinheiro/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export const getExpensesData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export const getExpensesRentData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/aluguel/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export const getExpensesAnesthesiaData = async (month="total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/anestesia/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}
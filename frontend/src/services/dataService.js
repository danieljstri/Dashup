import axios from 'axios';

/**
 * Fetches all data from the API.
 *
 * @async
 * @function getAllData
 * @returns {Promise<Object>} The data retrieved from the API.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getAllData = async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/all');
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches profit data for a specified month.
 *
 * @async
 * @function getProfitData
 * @param {string} [month="total"] - The month for which to retrieve profit data.
 * @returns {Promise<Object>} The profit data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getProfitData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/lucros/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches revenue data for a specified month.
 *
 * @async
 * @function getRevenueData
 * @param {string} [month="total"] - The month for which to retrieve revenue data.
 * @returns {Promise<Object>} The revenue data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getRevenueData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches revenue data for exams for a specified month.
 *
 * @async
 * @function getRevenueExamsData
 * @param {string} [month="total"] - The month for which to retrieve exam revenue data.
 * @returns {Promise<Object>} The exam revenue data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getRevenueExamsData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/exames/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches revenue data for anesthesia for a specified month.
 *
 * @async
 * @function getRevenueAnesthesiaData
 * @param {string} [month="total"] - The month for which to retrieve anesthesia revenue data.
 * @returns {Promise<Object>} The anesthesia revenue data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getRevenueAnesthesiaData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/anestesia/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches revenue data of consultations for a specified month.
 *
 * @async
 * @function getRevenueConsultationData
 * @param {string} [month="total"] - The month for which to retrieve cash revenue data.
 * @returns {Promise<Object>} The cash revenue data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getRevenueConsultationData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/receitas/consulta/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches expenses data for a specified month.
 *
 * @async
 * @function getExpensesData
 * @param {string} [month="total"] - The month for which to retrieve expenses data.
 * @returns {Promise<Object>} The expenses data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getExpensesData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches rent expenses data for a specified month.
 *
 * @async
 * @function getExpensesRentData
 * @param {string} [month="total"] - The month for which to retrieve rent expenses data.
 * @returns {Promise<Object>} The rent expenses data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getExpensesRentData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/aluguel/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches anesthesia expenses data for a specified month.
 *
 * @async
 * @function getExpensesAnesthesiaData
 * @param {string} [month="total"] - The month for which to retrieve anesthesia expenses data.
 * @returns {Promise<Object>} The anesthesia expenses data retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getExpensesAnesthesiaData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/despesas/anestesia/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches economic data for a specified company.
 *
 * @async
 * @function getEconomicCompanieData
 * @param {string} [company_name="DRA ISABELLY DE MORAIS LTDA"] - The name of the company.
 * @returns {Promise<Object>} The economic data for the specified company in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getEconomicCompanieData = async (company_name = "DRA ISABELLY DE MORAIS LTDA") => {
  try {
    // URL-encode the company name to handle spaces and special characters
    const encodedCompanyName = encodeURIComponent(company_name);
    const response = await axios.get(`http://localhost:3000/api/economia/${encodedCompanyName}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches markup data for anesthesia for a specified month.
 *
 * @async
 * @function getMarkupAnesthesiaData
 * @param {string} [month="total"] - The month for which to retrieve anesthesia markup data.
 * @returns {Promise<Object>} The anesthesia markup data retrieved from the API in the format { month: string, value: (number = fixed_expenses, number = variable_expenses, number = product_revenue) }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getMarkupAnesthesiaData = async (month = "total") => {
  try {
    const response = await axios.get(`http://localhost:3000/api/markup/anestesia/${month}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

/**
 * Fetches data for all economic companies.
 *
 * @async
 * @function getAllEconomicCompaniesData
 * @returns {Promise<Object>} The data for all economic companies retrieved from the API in the format { month: string, value: number }.
 * @throws Will throw an error if the HTTP request fails.
 */
export const getAllEconomicCompaniesData = async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/companies');
    return response.data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};
import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api";

// Post request
export const uploadEtf = (file: File) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_BASE_URL}/upload-etf`, formData);
};

// Get requests
export const getConstituents = () => axios.get(`${API_BASE_URL}/constituents`);
export const getEtfPrices = () => axios.get(`${API_BASE_URL}/etf-prices`);
export const getTopHoldings = () => axios.get(`${API_BASE_URL}/top-holdings`);

import axios from "axios";

const API = axios.create({
    baseURL: "http://192.168.29.89:8000"
});

export const getDashboardStats = () =>
    API.get("/dashboard/stats");

export const getTransactions = () =>
    API.get("/transactions/");

export const getAlerts = () =>
    API.get("/transactions/alerts");

export const getLogins = () =>
    API.get("/logins/");

export default API;
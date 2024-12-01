import axios from 'axios';

const API_BASE_URL_RANDOM = process.env.REACT_APP_RANDOM_MOVIES_URL || 'http://localhost:8003';
const API_BASE_URL_RECOMMENDER = process.env.REACT_APP_RECOMMENDER_URL || 'http://localhost:8002';

export const randomMoviesApi = axios.create({
  baseURL: API_BASE_URL_RANDOM,
});

export const recommenderApi = axios.create({
  baseURL: API_BASE_URL_RECOMMENDER,
});

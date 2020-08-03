import axios from 'axios'

let baseURL;

if (process.env.NODE_ENV === 'development') {
    baseURL = '/api';
} else if (process.env.NODE_ENV === 'production') {
    baseURL = '/api/interview';
}

axios.defaults.baseURL = baseURL

export default axios
import axios from 'axios'

let baseURL;

if (process.env.NODE_ENV === 'development') {
    baseURL = '/';
} else if (process.env.NODE_ENV === 'production') {
    baseURL = '/interview';
}

axios.defaults.baseURL = baseURL

export default axios
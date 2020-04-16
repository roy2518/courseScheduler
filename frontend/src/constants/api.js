import axios from "axios";

// Instantiate an axios client
export const client = axios.create({
    baseURL: "https://class-stage.herokuapp.com"
});
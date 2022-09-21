import { createApp } from "vue";
import App from "./App.vue";
require("@/assets/sass/main.scss");
import axios from "axios";
import router from "./router";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/"; // the FastAPI backend

createApp(App).use(router).mount("#app");

import { createApp } from "vue";
import App from "./App.vue";
require("@/assets/sass/main.scss");
import axios from "axios";
import router from "./router";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faArrowUp } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { BulmaExtensions } from "bulma-extensions";

library.add(faArrowUp);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/"; // the FastAPI backend

createApp(App)
  .use(router, BulmaExtensions)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");

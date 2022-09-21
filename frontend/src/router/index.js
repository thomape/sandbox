import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView";
import TestView from "@/views/TestView";

const routes = [
  {
    path: "/",
    name: "main",
    component: MainView,
  },
  {
    path: "/signin",
    name: "signin",
    component: () => import("@/views/SigninView"),
  },
  {
    path: "/test",
    name: "test",
    component: TestView,
  },
  {
    path: "/blog",
    name: "blog",
    component: () => import("@/views/BlogView"),
  },
  {
    path: "/store",
    name: "store",
    component: () => import("@/views/StoreView"),
  },
  {
    path: "/signup",
    name: "signup",
    component: () => import("@/views/SignupView"),
  },
  {
    path: "/contact",
    name: "contact",
    component: () => import("@/views/ContactView"),
  },
  {
    path: "/home",
    name: "home",
    component: () => import("@/views/HomeView"),
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/AboutView"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

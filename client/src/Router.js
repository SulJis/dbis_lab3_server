import Vue from "vue";
import VueRouter from 'vue-router';
import LoginPage from "@/pages/LoginPage";

Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {
            path: '',
            name: 'home',
            component: LoginPage,
        },

        {
            path: '/login',
            name: 'Login',
            component: LoginPage,
        },
    ],
    mode: 'history',
    history: true,
});


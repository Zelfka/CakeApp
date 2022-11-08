import Vue from "vue";
import VueRouter from "vue-router";
import CakesList from './views/CakesList'
import LogIn from "@/views/LogIn"
import LogOut from "@/views/LogOut";

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/cakes',
            name: 'cakes',
            component: CakesList,
        },
        {
            path: '/login',
            name: 'login',
            component: LogIn,
        },
        {
            path: '/logout',
            name: 'logout',
            component: LogOut,
        }
    ]
})
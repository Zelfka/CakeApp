import Vue from "vue"
import VueRouter from "vue-router"
import CakesList from './views/CakesList'
import LogIn from "@/views/LogIn"
import LogOut from "@/views/LogOut"
import RegisterUser from "@/views/RegisterUser"

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/cakes',
            name: 'cakes',
            component: CakesList,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/login',
            name: 'login',
            component: LogIn,
        },
         {
            path: '/register',
            name: 'register',
            component: RegisterUser,
        },
        {
            path: '/logout',
            name: 'logout',
            component: LogOut,
        }
    ]
})
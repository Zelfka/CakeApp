import Vue from "vue"
import VueRouter from "vue-router"
import CakesList from './views/CakesList'
import LogIn from "@/views/LogIn"
import LogOut from "@/views/LogOut"
import RegisterUser from "@/views/RegisterUser"
import UserProfile from "@/views/UserProfile"
import HomePage from "@/views/HomePage"
import UpdateProfile from "@/views/UpdateProfile"
import OneCake from "@/views/OneCake"
import CakesByOrder from "@/views/CakesByOrder"
import CreateCake from "@/views/CreateCake"

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomePage,
        },
        {
            path: '/cakes',
            name: 'cakes',
            component: CakesList,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/cakes/:id',
            name: 'one cake',
            component: OneCake,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/cakes/admin/add',
            name: 'create cake',
            component: CreateCake,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/profile/:id',
            name: 'profile',
            component: UserProfile,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/profile/:id/update',
            name: 'update profile',
            component: UpdateProfile,
            meta: {
                requiresLogin: true
            }
        },
         {
            path: '/order/:order_id',
            name: 'user order',
            component: CakesByOrder,
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
import Vue from "vue";
import VueRouter from "vue-router";
import CakesList from './views/CakesList'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/cakes',
            name: 'cakes',
            component: CakesList,
        }
    ]
})
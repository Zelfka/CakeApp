import Vue from "vue";
import Vuex from 'vuex'
import {getAPI} from "@/axios-api";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
        APIData: ''
    },
    mutations: {
        updateStorage(state, { access, refresh}){
            state.accessToken = access
            state.refreshToken = refresh
        },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
        }
    },
    getters: {
        loggedIn (state) {
            return state.accessToken != null
        }
    },
    plugins: [createPersistedState()],
    actions: {
        userLogin (context, credentials) {
            return new Promise(resolve => {
                getAPI.post('api/login/', {
                    username: credentials.username,
                    password: credentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh})
                        resolve()
                    })
            })
        },

        userLogout (context) {
            return new Promise((resolve) => {
                if(context.getters.loggedIn){
                    getAPI.post('api/logout/')
                    .then(() => {
                        context.commit('destroyToken')
                        resolve()
                    })
                        .catch(err => {
                            console.log(err)
                        })
                } else {
                    resolve()
                }

            })
        }
    }
})
import Vue from "vue";
import Vuex from 'vuex'
import {getAPI} from "@/axios-api";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
        APIData: '',
        id: null,
        admin: false
    },
    mutations: {
        updateStorage(state, { access, refresh, id, admin}){
            state.accessToken = access
            state.refreshToken = refresh
            state.id = id
            state.admin = admin
        },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
            state.id = null
            state.admin = false
        }
    },
    getters: {
        loggedIn (state) {
            return state.accessToken != null
        },
        adminUser (state) {
            return state.admin === true
        }
    },
    plugins: [createPersistedState()],
    actions: {
        userLogin (context, credentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('api/login/', {
                    username: credentials.username,
                    password: credentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh, id: response.data.id, admin: response.data.admin})
                        resolve()
                    })
                    .catch(err => {
                        reject(err.response.data.detail)
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
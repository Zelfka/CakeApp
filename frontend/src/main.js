import Vue from 'vue'
import App from './App.vue'
import router from './routes'
import store from './store.js'
import IdleVue from 'idle-vue'
import moment from 'moment'
import JwPagination from 'jw-vue-pagination'

const eventsHub = new Vue()
Vue.component('jw-pagination', JwPagination);
Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 1800000
})

Vue.config.productionTip = false
Vue.prototype.moment = moment
router.beforeEach((to, from, next) => {
  if (to.matched.some( record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login'})
    } else {
      next()
    }
  } else {
    next()
  }
})
router.beforeEach((to, from, next) => {
  if (to.matched.some( record => record.meta.isAdmin)) {
    if (!store.getters.adminUser) {
      next ( {name: 'home'})
    } else {
      next()
    }
  } else {
    next()
  }
})
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

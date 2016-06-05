import Vue from 'vue'
import Vuex from 'vuex'
import Router from 'vue-router'
import Resource from 'vue-resource'
import IndexView from './views/IndexView'
import ShopView from './views/ShopView'
import OrderView from './views/OrderView'
import LoginView from './views/LoginView'
import Register from './views/RegisterView'
import App from './App'

Vue.use(Router)
Vue.use(Vuex)
Vue.use(Resource)
// fix post https://github.com/vuejs/vue-resource/blob/master/docs/config.md
Vue.http.options.emulateJSON = true
// routing
var router = new Router()

router.map({
  '/index': {
    component: IndexView
  },
  '/shop/:shopId': {
    name: 'shop',
    component: ShopView,
    shop: true
  },
  '/order': {
    component: OrderView
  },
  '/user_login': {
    component: LoginView
  },
  '/register': {
    component: Register
  }
})

router.redirect({
  '/': '/index'
})

router.beforeEach(function () {
  window.scrollTo(0, 0)
})

router.start(App, '#app')

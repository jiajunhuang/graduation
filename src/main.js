import Vue from 'vue'
import Vuex from 'vuex'
import Router from 'vue-router'
import IndexView from './views/IndexView.vue'
import ShopView from './views/ShopView.vue'
import OrderView from './views/OrderView.vue'
import App from './App'

Vue.use(Router)
Vue.use(Vuex)

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
  }
})

router.redirect({
  '/': '/index'
})

router.beforeEach(function () {
  window.scrollTo(0, 0)
})

router.start(App, '#app')

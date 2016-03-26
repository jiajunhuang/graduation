import Vue from 'vue'
import Router from 'vue-router'
import IndexView from './components/IndexView.vue'
import ShopView from './components/ShopView.vue'
import UserView from './components/UserView.vue'
import App from './App'

Vue.use(Router)

// routing
var router = new Router()

router.map({
  '/index': {
    component: IndexView
  },
  '/user/': {
    component: UserView
  },
  '/shop/:id': {
    component: ShopView
  }
})

router.redirect({
  '*': '/index'
})

router.beforeEach(function () {
  window.scrollTo(0, 0)
})

router.start(App, '#app')

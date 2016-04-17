import Vue from 'vue'
import Vuex from 'vuex'
import cart from './modules/cart'

Vue.use(Vuex)
Vue.config.debug = true

export default new Vuex.Store({
  modules: {
    cart
  }
})

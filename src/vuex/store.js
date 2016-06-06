import Vue from 'vue'
import Vuex from 'vuex'
import cart from './modules/cart'
import excavator from './modules/excavator'
import user from './modules/user'

Vue.use(Vuex)
Vue.config.debug = true

export default new Vuex.Store({
  modules: {
    cart,
    excavator,
    user
  }
})

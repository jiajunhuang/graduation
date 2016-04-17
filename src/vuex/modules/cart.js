import {
  ADD_TO_CART
} from '../mutation-types'

const state = {
  foods: []
}

const mutations = {
  [ADD_TO_CART](state, food) {
    state.foods.push(food)
    console.log(state.foods)
  }
}

export default {
  state,
  mutations
}

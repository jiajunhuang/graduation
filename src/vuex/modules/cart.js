import {
  ADD_TO_CART,
  DELETE_ALL
} from '../mutation-types'

const state = {
  foods: [],
  sum: 0
}

const mutations = {
  [ADD_TO_CART](state, food) {
    const record = state.foods.find(p => p.fid === food.fid)
    if (!record === true) {
      food.quantity = 1
      state.foods.push(food)
    } else {
      food.quantity = food.quantity + 1
    }
    state.sum = state.sum + 1
  },
  [DELETE_ALL](state) {
    state.foods.length = 0
    state.sum = 0
  }
}

export default {
  state,
  mutations
}

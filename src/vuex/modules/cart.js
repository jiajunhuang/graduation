import {
  ADD_TO_CART,
  DELETE_ALL,
  PLUS_FOOD_QUANTITY,
  MINUS_FOOD_QUANTITY,
  UPDATE_FOOD_QUANTITY
} from '../mutation-types'

const state = {
  foods: [],
  num: 0
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
    state.num = state.num + 1
  },
  [PLUS_FOOD_QUANTITY](state, food) {
    let index = state.foods.indexOf(food)
    food.quantity = food.quantity + 1
    state.num = state.num + 1
    state.foods.splice(index, 1, food)
  },
  [MINUS_FOOD_QUANTITY](state, food) {
    let index = state.foods.indexOf(food)
    food.quantity = food.quantity - 1
    state.num = state.num - 1
    if (food.quantity === 0) {
      state.foods.splice(index, 1)
    }
  },
  [UPDATE_FOOD_QUANTITY](state, food, currentNum) {
    let index = state.foods.indexOf(food)
    food.quantity = currentNum
    if (food.quantity === 0) {
      state.foods.splice(index, 1)
    } else {
      state.foods.splice(index, 1, food)
    }
  },
  [DELETE_ALL](state) {
    state.foods.length = 0
    state.num = 0
  }
}

export default {
  state,
  mutations
}

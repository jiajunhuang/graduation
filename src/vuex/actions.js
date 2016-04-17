import * as types from './mutation-types'

export const addToCart = ({ dispatch }, food) => {
  dispatch(types.ADD_TO_CART, food)
}

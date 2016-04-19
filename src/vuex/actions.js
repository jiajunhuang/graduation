import * as types from './mutation-types'

export const addToCart = ({ dispatch }, food) => {
  dispatch(types.ADD_TO_CART, food)
}

export const deleteAll = ({ dispatch }) => {
  dispatch(types.DELETE_ALL)
}

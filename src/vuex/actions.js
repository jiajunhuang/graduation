import * as types from './mutation-types'

export const addToCart = ({ dispatch }, food) => {
  dispatch(types.ADD_TO_CART, food)
}

export const deleteAll = ({ dispatch }) => {
  dispatch(types.DELETE_ALL)
}

export const updateState = ({ dispatch }, data) => {
  dispatch(types.UPDATE_STATE, data)
}

export const sortByDefault = ({ dispatch }) => {
  dispatch(types.SORT_BY_DEFAULT)
}

export const sortBySalesCount = ({ dispatch }) => {
  dispatch(types.SORT_BY_SALES_COUNT)
}

export const sortByGrade = ({ dispatch }) => {
  dispatch(types.SORT_BY_GRADE)
}

export const sortByLowestMoney = ({ dispatch }) => {
  dispatch(types.SORT_BY_LOWEST_MONEY)
}

export const filterShops = ({ dispatch }, sortKeys) => {
  dispatch(types.FILTER_SHOPS, sortKeys)
}

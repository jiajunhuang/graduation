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

export const sortByDefault = ({ dispatch }, shops) => {
  dispatch(types.SORT_BY_DEFAULT, shops)
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

export const filterByIsNewer = ({ dispatch }) => {
  dispatch(types.FILTER_BY_IS_NEWER)
}

export const filterByFreeDeliver = ({ dispatch }) => {
  dispatch(types.FILTER_BY_IS_FREE_DELIVER)
}

export const filterByIsInvoice = ({ dispatch }) => {
  dispatch(types.FILTER_BY_IS_INVOICE)
}

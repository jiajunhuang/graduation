import {
  SORT_BY_DEFAULT,
  SORT_BY_SALES_COUNT,
  SORT_BY_GRADE,
  SORT_BY_LOWEST_MONEY,
  FILTER_BY_IS_NEWER,
  FILTER_BY_IS_FREE_DELIVER,
  FILTER_BY_IS_INVOICE
} from '../mutation-types'

const state = {
  type: 'default'
}

const mutations = {
  [SORT_BY_DEFAULT](state) {
    console.log(state)
  },
  [SORT_BY_SALES_COUNT](state) {
    console.log(state)
  },
  [SORT_BY_GRADE](state) {
    console.log(state)
  },
  [SORT_BY_LOWEST_MONEY](state) {
    console.log(state)
  },
  [FILTER_BY_IS_NEWER](state) {
    console.log(state)
  },
  [FILTER_BY_IS_FREE_DELIVER](state) {
    console.log(state)
  },
  [FILTER_BY_IS_INVOICE](state) {
    console.log(state)
  }

}

export default {
  state,
  mutations
}

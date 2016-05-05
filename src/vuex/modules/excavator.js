import {
  UPDATE_STATE,
  SORT_BY_DEFAULT,
  SORT_BY_SALES_COUNT,
  SORT_BY_GRADE,
  SORT_BY_LOWEST_MONEY,
  FILTER_BY_IS_NEWER,
  FILTER_BY_IS_FREE_DELIVER,
  FILTER_BY_IS_INVOICE
} from '../mutation-types'
import Immutable from 'immutable'


const state = {
  type: SORT_BY_DEFAULT,
  shops: [],
  initialShops: []
}

const mutations = {
  [UPDATE_STATE](state, data) {
    state.initialShops = Immutable.List(data.shops)
    state.shops = state.initialShops.toArray()
  },
  [SORT_BY_DEFAULT](state) {
    state.shops = state.initialShops.toArray()
  },
  [SORT_BY_SALES_COUNT](state) {
    state.shops = state.initialShops.toArray().sort((a, b) => { return (a.sales_count >= b.sales_count) ? -1 : 1 })
  },
  [SORT_BY_GRADE](state) {
    state.shops = state.initialShops.toArray().sort((a, b) => { return (a.avg_grade >= b.avg_grade) ? -1 : 1 })
  },
  [SORT_BY_LOWEST_MONEY](state) {
    state.shops = state.initialShops.toArray().sort((a, b) => { return (a.lowest_money >= b.lowest_money) ? 1 : -1 })
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

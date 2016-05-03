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

const state = {
  shops: [],
  initData: {}
}

const compare = (a,  b, key) => {
  if ((a.key === undefined) || (b.key === undefined)) throw Error('compare:key undefined.')
  if (a.key - b.key > 0) {
    return -1
  }
  if (a.key - b.key < 0) {
    return 1
  }
  return 0
}

const mutations = {
  [UPDATE_STATE](state, data) {
    console.log(data)
    state.shops = data.shops
    state.initData = Object.assign({}, data)
  },
  [SORT_BY_DEFAULT](state) {
    console.log(state)
    // state.shops = shops
  },
  [SORT_BY_SALES_COUNT](state) {
    state.shops.sort((a, b) => {
      if (a.sales_count - b.sales_count > 0) {
        return -1
      }
      if (a.sales_count - b.sales_count < 0) {
        return 1
      }
      return 0
    })
  },
  [SORT_BY_GRADE](state) {
    state.shops.sort((a, b) => {
      if (a.sales_count - b.sales_count > 0) {
        return -1
      }
      if (a.sales_count - b.sales_count < 0) {
        return 1
      }
      return 0
    })
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

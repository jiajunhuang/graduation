import {
  UPDATE_STATE,
  SORT_BY_DEFAULT,
  SORT_BY_SALES_COUNT,
  SORT_BY_GRADE,
  SORT_BY_LOWEST_MONEY,
  FILTER_SHOPS
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
    state.shops = state.initialShops.toArray().sort((a, b) => a.sales_count >= b.sales_count ? -1 : 1)
  },
  [SORT_BY_GRADE](state) {
    state.shops = state.initialShops.toArray().sort((a, b) => a.avg_grade >= b.avg_grade ? -1 : 1)
  },
  [SORT_BY_LOWEST_MONEY](state) {
    state.shops = state.initialShops.toArray().sort((a, b) => a.lowest_money >= b.lowest_money ? 1 : -1)
  },
  [FILTER_SHOPS](state, sortKeys) {
    state.shops = state.initialShops.toArray()
    if (sortKeys.indexOf('newer') > -1) {
      state.shops = state.shops.filter(shop => shop.new_seller === true)
    }
    if (sortKeys.indexOf('free') > -1) {
      state.shops = state.shops.filter(shop => shop.free_send === true)
    }
    if (sortKeys.indexOf('invoice') > -1) {
      state.shops = state.shops.filter(shop => shop.invoice === true)
    }
  }
}

export default {
  state,
  mutations
}

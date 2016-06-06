import {
  SET_UID
} from '../mutation-types'

const state = {
  uid: 0
}

const mutations = {
  [SET_UID](state, uid) {
    state.uid = uid
  }
}

export default {
  state,
  mutations
}

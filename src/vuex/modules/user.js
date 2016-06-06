import {
  SET_UID,
  SET_UNAME
} from '../mutation-types'

const state = {
  uid: 0,
  uname: ''
}

const mutations = {
  [SET_UID](state, uid) {
    state.uid = uid
  },
  [SET_UNAME](state, name) {
    state.uname = name
  }
}

export default {
  state,
  mutations
}

import {
  SET_UID,
  SET_UNAME,
  SET_ADDRESS
} from '../mutation-types'

const state = {
  uid: 0,
  uname: '',
  address: ''
}

const mutations = {
  [SET_UID](state, uid) {
    state.uid = uid
  },
  [SET_UNAME](state, name) {
    state.uname = name
  },
  [SET_ADDRESS](state, address) {
    state.address = address
  }
}

export default {
  state,
  mutations
}

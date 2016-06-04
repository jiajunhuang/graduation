<template>
  <top-header></top-header>
  <router-view></router-view>
  <bottom-footer></bottom-footer>
</template>

<script>
import store from './vuex/store'
import TopHeader from './components/Header'
import BottomFooter from './components/Footer'
import IndexView from './views/IndexView'
import ShopView from './views/ShopView'
import OrderView from './views/ShopView'

export default {
  name: 'App',
  components: [
    TopHeader, IndexView, ShopView, OrderView, BottomFooter
  ],
  store
}
</script>
<style lang='sass'>

@import './assets/base';

body {
  // height: 5000px;
  background-color: #f7f7f7;
}

</style>

<template>
  <top-header></top-header>
  <router-view></router-view>
</template>

<script>
import store from './vuex/store'
import TopHeader from './components/Header.vue'
import IndexView from './views/IndexView.vue'
import ShopView from './views/ShopView.vue'

export default {
  name: 'App',
  components: [
    TopHeader, IndexView, ShopView
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

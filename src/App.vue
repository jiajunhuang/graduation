<template>
  <top-header></top-header>
  <router-view></router-view>
</template>

<script>

import TopHeader from './components/Header.vue'
import IndexView from './components/IndexView.vue'

export default {
  name: 'App',
  components: [
    TopHeader, IndexView
  ]
}
</script>
<style lang='sass'>

@import './assets/base';

body {
  height: 5000px;
}

</style>

<template>
  <top-header></top-header>
  <!-- <router-view>
  </router-view> -->
  <!-- <footer>

  </footer> -->
  <fixed-navbar></fixed-navbar>
</template>

<script>

import TopHeader from './components/Header.vue'
import FixedNavbar from './components/FixedNavbar.vue'

export default {
  name: 'App',
  components: {
    TopHeader,
    FixedNavbar
  }
}
</script>
<style lang='sass'>

@import './assets/base';

</style>

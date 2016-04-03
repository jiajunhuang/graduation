<template>
  <sliders></sliders>
  <excavator></excavator>
  <index-shop-item></index-shop-item>
  <fixed-navbar></fixed-navbar>
</template>

<script>
import Sliders from '../components/Sliders'
import FixedNavbar from '../components/FixedNavbar'
import Excavator from '../components/Excavator'
import IndexShopItem from '../items/IndexShopItem'


export default {
  name: 'IndexView',
  components: [ Sliders, FixedNavbar, Excavator, IndexShopItem ]
}
</script>

<style lang="sass" scoped>

</style>

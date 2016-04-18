<template>
  <sliders></sliders>
  <excavator></excavator>
  <index-shop-item></index-shop-item>
  <cart></cart>
</template>

<script>
import Sliders from '../components/Sliders'
import Cart from '../components/Cart'
import Excavator from '../components/Excavator'
import IndexShopItem from '../items/IndexShopItem'


export default {
  name: 'IndexView',
  components: [ Sliders, Cart, Excavator, IndexShopItem ]
}
</script>

<style lang="sass" scoped>

</style>

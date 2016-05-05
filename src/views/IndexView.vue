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
import { updateState } from '../vuex/actions'
export default {
  name: 'IndexView',
  components: [ Sliders, Cart, Excavator, IndexShopItem ],
  ready() {
    fetch('/shop/all?page_size=32').then(response => {
      return response.json()
    }).then((json) => {
      this.updateState(json)
    })
  },
  vuex: {
    actions: {
      updateState
    }
  }
}
</script>

<style lang="sass" scoped>

</style>

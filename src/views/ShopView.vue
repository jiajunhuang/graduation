<template >
  <shop-item></shop-item>
  <cart></cart>
</template>

<script>
import Cart from '../components/Cart'
import ShopItem from '../items/ShopItem'

export default {
  name: 'ShopView',
  components: [ Cart, ShopItem ]
}

</script>

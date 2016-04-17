<template >
  <shop-item></shop-item>
  <fixed-navbar></fixed-navbar>
</template>

<script>
import FixedNavbar from '../components/FixedNavbar'
import ShopItem from '../items/ShopItem'

export default {
  name: 'ShopView',
  components: [ FixedNavbar, Grade ]
}

</script>

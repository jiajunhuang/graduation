<template>
  <order></order>
  <cart></cart>
</template>

<script>
import Order from '../components/Order'
import Cart from '../components/Cart'
export default {
  name: 'OrderView',
  components: [ Order, Cart ]
}

</script>

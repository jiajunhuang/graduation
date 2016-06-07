<template>
  <address></address>
  <cart></cart>
</template>

<script>
import Address from '../components/Address'
import Cart from '../components/Cart'
export default {
  name: 'AddressView',
  components: [ Address, Cart ]
}

</script>

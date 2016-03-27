<template>
  <sliders></sliders>
  <h2>index</h2>
  <fixed-navbar></fixed-navbar>
</template>

<script>
import Sliders from './Sliders.vue'
import FixedNavbar from './FixedNavbar.vue'

export default {
  name: 'IndexView',
  components: [ Sliders, FixedNavbar ]
}
</script>

<style lang="sass">

</style>

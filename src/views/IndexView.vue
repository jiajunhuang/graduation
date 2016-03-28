<template>
  <sliders></sliders>
  <excavator></excavator>
  <fixed-navbar></fixed-navbar>
</template>

<script>
import Sliders from '../components/Sliders'
import FixedNavbar from '../components/FixedNavbar'
import Excavator from '../components/Excavator'

export default {
  name: 'IndexView',
  components: [ Sliders, FixedNavbar, Excavator ]
}
</script>

<style lang="sass" scoped>

</style>

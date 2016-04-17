<template >
  <span class="grade">{{ gradeData }}</span>
</template>

<style lang="sass" scoped>
  span.grade {
    color: #ffc30c;
  }
</style>

<script>
  export default {
    name: 'Grade',
    props: ['number'],
    computed: {
      gradeData: function () {
        return '\u2605'.repeat(this.number)
      }
    }
  }
</script>

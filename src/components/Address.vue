<template>
  <div class="container address">
    <h3>地址管理</h3>
    <div class="content">
      <p v-show="isShowEditor === false">地址：{{ address }}</p>
      <label v-show="isShowEditor === true">地址：<input type="text" v-model="address"></label>
    </div>
    <div class="control">
      <a v-show="isShowEditor === false" href="#" v-on:click.prevent="toggleEditor()">修改</a>
      <a v-show="isShowEditor === true" href="#" v-on:click.prevent="saveAddress()">保存</a>
    </div>
  </div>
</template>

<style lang='sass' scoped>
  div.container.address {
    width: 1000px;
    margin: 0 auto;
    margin-top: 20px;
    border: 1px solid #eee;
    background-color: #fff;
    min-height: 680px;
    padding: 20px 18px;
  }
  h3 {
    border-bottom: 2px solid #f4f4f4;
    padding: 0 20px 11px;
    font-size: 18px;
    font-weight: 700;
  }
  div.content {
    margin-top: 30px;
  }
  div.control {
    margin-top: 30px;
  }
</style>

<script>
import { user } from '../vuex/getters'
import { setAddress } from '../vuex/actions'
export default {
  name: 'Address',
  data() {
    return {
      address: '',
      isShowEditor: false
    }
  },
  methods: {
    toggleEditor() {
      this.isShowEditor = true
    },
    saveAddress() {
      this.setAddress(this.address)
      this.isShowEditor = false
    }

  },
  vuex: {
    getters: {
      user
    },
    actions: {
      setAddress
    }
  }
}
</script>

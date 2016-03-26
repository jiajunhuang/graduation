<template>
  <div class="fixed-navbar">
    <div class="container">
      <div class="order">
        <a v-link="{  path: 'order' }" class="item">※</a>
        <span class="tips">我的订单</span>
      </div>
      <div class="shopping-cart">
        <a href="#"  v-on:click="" class="item">购物车</a>
      </div>
    </div>
  </div>
</template>

<style lang='sass' scoped>

$height: 200px;
$bgColor: #504d53;
$fontColor: #ccc;
div.fixed-navbar {
  position: fixed;
  right: 0px;
  top: 0px;
  bottom: 0px;
  width: 35px;
  height: 100%;
  display: inline-block;
  background-color: $bgColor;

  div.container {
    height: $height;
    position: absolute;
    top: 50%;
    margin-top: -$height * 0.5;
    a.item {
      display: block;
      text-align: center;
      color: $fontColor;
      line-height: 16px;
      padding: 7px 8px 10px;
      margin-bottom: 8px;
      margin-top: 8px;
      font-size: 14px;
      font-weight: 700;
      text-decoration: none;

      &:hover {
        background-color: #26a2ff;
        color: #fff;
        outline: 0;
      }
    }
    div.order {
      position: relative;
      .tips {
        display: none;
      }
      &:hover {
        .tips {
          display: block;

        }
      }
    }
    span.tips {
      position: absolute;
      right: 50px;
      top: -1px;
      width: 5em;
      padding: 0.2em 0.5em;
      border-radius: 2px;
      background-color: $bgColor;
      color: $fontColor;
      &:after {
        content: ' ';
        border: 5px solid $bgColor;
        display: block;
        position: absolute;
        top: 10px;
        border-color: transparent transparent transparent $bgColor;
        right: -10px;
      }
    }
  }
}
</style>

<script>
export default {
  name: 'FixedNavbar'
}
</script>

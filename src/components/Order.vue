<template>
  <div class="container order">
    <h3>我的订单</h3>
    <div class="no-data">
      <p >暂无记录，现在就去<a v-link="{ path: '/index' }">订餐</a>吧!</p>
    </div>
  </div>
</template>

<style lang='sass' scoped>
  div.container.order {
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
  div.no-data {
    padding-top: 50px;
    text-align: center;
    p {
      display: inline-block;
      padding-left: 110px;
      line-height: 115px;
      background: url("../assets/nodata.png") no-repeat;
      color: #999;
      a {
        margin: 0 5px;
      }
    }
  }
</style>

<script>
export default {
  name: 'Order'
}
</script>

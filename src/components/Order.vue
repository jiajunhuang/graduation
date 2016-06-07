<template>
  <div class="container order">
    <h3 calss="title">我的订单</h3>
    <div class="no-data" v-show="deals.length === 0">
      <p >暂无记录，现在就去<a v-link="{ path: '/index' }">订餐</a>吧!</p>
    </div>
    <div class="has-data" v-show="deals.length !== 0">
      <table class="order-list">
        <thead>
          <tr>
            <th>下单时间</th>
            <th class="order-list-infoth">订单内容</th>
            <th></th>
            <th>支付金额（元）</th>
            <th>状态</th>
          </tr>
        </thead>
        <tbody>
          <tr class="timeline">
            <td class="ordertimeline-time">
              <p class="ordertimeline-title">{{ shop.sellTime[0] }}</p>
              <p>{{ shop.sellTime[1] }}</p>
            </td>
            <td class="ordertimeline-avatar">
              <a v-link="{ path: '/shop/' + shop.id }" >
                <img v-bind:src="shop.avatar">
              </a>
            </td>
            <td class="ordertimeline-info">
              <h3 class="ordertimeline-title">
                <a v-link="{ path: '/shop/' + shop.id }" >{{ shop.name }}</a>
              </h3>
              <p class="ordertimeline-info-food">
                <a >
                  <span class="ordertimeline-info-productnum" >{{ deals.length }}</span>
                  <span>个菜品</span>
                </a>
              </p>
              <p>订单号: {{ did }}</p>
            </td>
            <td class="ordertimeline-amount">
              <h3 class="ordertimeline-title ordertimeline-price">{{ sumPrice }}</h3>
            </td>
            <td class="ordertimeline-status">
              <h3 class="waitpay">制作中</h3>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</template>

<script>
import { user } from '../vuex/getters'
export default {
  name: 'Order',
  data() {
    return {
      deals: [],
      did: 0,
      sumPrice: 0,
      shop: {
        sellTime: [0, 0],
        name: '',
        id: 0,
        avatar: ''
      }
    }
  },
  ready() {
    this.$http.get('/user/' + this.user.uid + '/deals').then((response) => {
      let data = response.data
      if (data.status === 1) {
        console.info('网络错误！')
        return false
      }
      this.deals = data.deals
      this.did = this.deals[0].did
      this.shop = {
        sellTime: this.deals[0].sell_at.split(' '),
        name: this.deals[0].seller.name,
        id: this.deals[0].seller.uid,
        avatar: this.deals[0].seller.avatar
      }
      this.sumPrice = this.deals.reduce((previous, current) => (
        previous + current.food.price
      ), 0)
    })
  },
  vuex: {
    getters: {
      user
    }
  }
}
</script>

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
  h3.title {
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
  div.has-data {
    margin-top: 50px;
  }
  .order-list {
    width: 100%;
    word-break: break-all;
    word-wrap: break-word;
  }
  .order-list tr:first-child {
    height: 10px;
  }
  .order-list thead tr {
    line-height: 30px;
    background-color: #eee;
  }
  .order-list td, 
  .order-list th {
    text-align: center;
    font-size: 12px;
  }
  .timeline td.ordertimeline-time {
    text-align: right;
    padding-right: 22px;
  }
  .order-list td, .order-list th {
    text-align: center;
    font-size: 12px;
  }
  .timeline td {
    padding-top: 30px;
    padding-bottom: 30px;
  }
  .ordertimeline-time {
    position: relative;
    width: 10%;
    color: #999;
    border-right: 1px #eee solid;
  }
  .ordertimeline-time p:first-child {
    font-size: 16px;
  }
  .ordertimeline-title {
    margin-bottom: 5px;
    font-weight: 700;
    font-size: 14px;
    color: #333;
  }
  .ordertimeline-price {
    margin-bottom: 0px;
  }
  .order-list td, 
  .order-list th {
    text-align: center;
    font-size: 12px;
  }
  .ordertimeline-avatar {
    padding-left: 37px;
    padding-right: 16px;
    width: 70px;
  }
  .timeline td.ordertimeline-info {
    text-align: left;
  }
  .ordertimeline-info a {
    color: inherit;
    text-decoration: none;
  }
  .ordertimeline-food, 
  .ordertimeline-info-food span {
    vertical-align: middle;
  }
  @media (min-width: 1260px) {
    .ordertimeline-food {
      max-width: 300px;
    }
  }
  
  .ordertimeline-food {
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    max-width: 200px;
    word-wrap: normal;
  }
  .order-list td, .order-list th {
    text-align: center;
    font-size: 12px;
  }
  .timeline td {
    padding-top: 30px;
    padding-bottom: 30px;
  }
  .ordertimeline-amount, 
  .ordertimeline-info, 
  .ordertimeline-status {
      border-bottom: 1px #eee dashed;
      color: #999;
  }
  .ordertimeline-status h3.waitpay {
      color: #ff9c00;
  }
  .order-list td, 
  .order-list th {
      text-align: center;
      font-size: 12px;
  }
  .timeline td {
      padding-top: 30px;
      padding-bottom: 30px;
  }
  .ordertimeline-amount, 
  .ordertimeline-handle, 
  .ordertimeline-status {
      width: 13%;
  }
  .ordertimeline-amount, 
  .ordertimeline-info, 
  .ordertimeline-status {
      border-bottom: 1px #eee dashed;
      color: #999;
  }
  .order-list td, 
  .order-list th {
      text-align: center;
      font-size: 12px;
  }
  .timeline td {
    padding-top: 30px;
    padding-bottom: 30px;
  }
  .ordertimeline-handle {
    border-bottom: 1px #eee dashed;
  }
  .ordertimeline-avatar img {
    width: 70px;
    height: 70px;
    border-radius: 50%;
  }
</style>



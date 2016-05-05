<template >
<div class="shop-items-container clearfix" v-on:click.stop>
  <loading :is-show-loading="shops.length === 0"></loading>
  <a class="item" v-for="shop in shops" track-by="uid" v-link="'shop/' + shop.uid">
    <div class="logo">
      <img v-bind:src="shop.avatar" v-bind:alt="shop.name" width="70" height="70"/>
      <span class="speed">{{* shop.speed}} 分钟</span>
    </div>
    <div class="content">
      <h4>{{* shop.name }}</h4>
      <p class="grade slice"><grade v-bind:number="shop.avg_grade"></grade></p>
      <p class="count slice">月售 {{* shop.sales_count }} 单</p>
      <p class="spend slice">{{* shop.lowest_money }}元起送</p>
    </div>
  </a>
</div>
</template>

<style lang="sass" scoped>

div.shop-items-container {
  width: 1000px;
  margin: 20px auto 0 auto;
  border: 1px solid #e6e6e6;
}

.item {
  float: left;
  width: 25%;
  height: 140px;
  background-color: #FFF;
  border-bottom: 1px solid #f5f5f5;
  display: block;
  cursor: pointer;
  text-decoration: none;
  color: #333;
  &:hover {
    background-color: #f5f5f5;
    h4 {
      color: #0089dc;
    }
  }
  .logo {

    float: left;
    padding: 20px;
    color: #999;
    font-size: 10pt;
    text-align: center;
    img {
      margin-bottom: 10px;
      display: block;
      width: 70px;
      height: 70px;
    }
    .speed {
      text-align: center;

    }
  }
  .content {
    padding: 20px;
    h4 {
      font-size: 1pc;
      margin-bottom: 6px;
      font-weight: 600;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
    .slice {
      color: #999;
      margin-left: 10px;
      margin-bottom: 4px;
      font-size: 10pt;
    }
  }
}

</style>

<script>
import Grade from 'components/Grade'
import Loading from 'components/Loading'
import { indexShops } from '../vuex/getters'
export default {
  name: 'IndexShopItem',
  components: [ Grade, Loading ],
  data() {
    return {
      isShowLoading: true
    }
  },
  vuex: {
    getters: {
      shops: indexShops
    }
  }
}
</script>

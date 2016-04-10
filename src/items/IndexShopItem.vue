<template >
<div class="shop-items-container clearfix">
  <a class="item" v-for="item in items" track-by="$index" v-link="'shop/' + item.uid">
    <div class="logo">
      <img v-bind:src="item.avatar" alt="" width="70" height="70"/>
      <span class="speed">{{* item.speed}} 分钟</span>
    </div>
    <div class="content">
      <h4>{{* item.name }}</h4>
      <p class="grade slice">{{* item.avg_grade | transStars }}</p>
      <p class="count slice">月售{{* item.sales_count }}单</p>
      <p class="spend slice">{{* item.lowest_money}}元起送</p>
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
  export default {
    name: 'IndexShopItem',
    data() {
      return {
        items: []
      }
    },
    ready() {
      fetch('/shop/all').then(response => {
        return response.json()
      }).then(json => {
        this.items = json.shops
      })
    },
    filters: {
      transStars(length) {
        return '⭐️'.repeat(length)
      }
    }

  }
</script>

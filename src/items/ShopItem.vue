<template >
  <div class="shop-item" v-on:click.stop>
    <div class="shop-guide">
      <div class="container">
        <div class="info">
          <img v-bind:src="shop.avatar" v-bind:alt="shop.name">
          <div class="detail">
            <h1 v-on:click="add()">{{ shop.name  }}</h1>
            <p class="grade slice"><grade v-bind:number="shop.avg_grade"></grade></p>
            <p class="count slice">月售 {{ shop.lowest_money }} 单</p>
          </div>
        </div>
        <div class="server">
          <span><em>起送价</em><em class="value">{{ shop.lowest_money }} 元</em></span>
          <span><em>平均送达时间</em><em class="value">{{ shop.speed }} 分钟</em></span>
        </div>
      </div>
    </div>
    <div class="shop-foods">
      <div class="foods-container">
        <h2>新品推荐</h2>
        <div class="food" v-for="food in foods" track-by="$index">
          <div class="image">
            <img v-bind:src="food.image" v-bind:alt="food.name">
          </div>
          <div class="intro">
            <h3>{{ food.name }}</h3>
            <p class="content">{{ food.name }}</p>
            <p class="grade"><grade v-bind:number="food.avg_grade"></grade></p>
          </div>
          <div class="price"><span>￥</span>{{ food.price }}</div>
          <div class="add-to-cart">
            <button v-on:click="addToCart(food)">加入购物车</button>
          </div>
        </div>
      </div>
      <div class="billboard">
        <div class="container">
          <h3>商家公告</h3>
          <p>尊敬的客户订餐也可以打电话13482278323</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Grade from '../components/Grade'
import { addToCart } from '../vuex/actions'
// import { cartProducts } from '../vuex/getters'

export default {
  name: 'ShopItem',
  components: [ Grade ],
  data() {
    return {
      shop: {},
      foods: []
    }
  },
  ready() {
    this.shopId = this.$route.params.shopId
    fetch('/shop/' + this.shopId).then(response => {
      return response.json()
    }).then(json => {
      this.shop = json
    })

    fetch('/shop/' + 12 + '/foods').then(response => {
      return response.json()
    }).then(json => {
      this.foods = json.foods
    })
  },
  methods: {
    add(foodId) {
      console.log(foodId)
    }
  },
  vuex: {
    // getters: {
    //   cartProducts
    // },
    actions: {
      addToCart
    }
  }
}

</script>

<style lang="sass" scoped>

div.shop-guide {
  background-image: url('../assets/shop-bg.jpg');
  background-size: cover;
  padding-top: 3pc;
  div.container {
    height: 142px;
    display: table;
    position: relative;
    width: 1000px;
    margin: 0 auto;
  }
  div.info {
    width: 400px;
    > img {
      margin-right: 15px;
      width: 95px;
      height: 95px;
      border-radius: 50%;
      border: 4px solid #fff;
      border: 4px solid rgba(255,255,255,.3);
      vertical-align: middle;
    }
  }
  div.detail {
    display: inline-block;
    vertical-align: middle;
    h1 {
      font-size: 20px;
      max-width: 270px;
      display: inline-block;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }
  }

  div.info {
    position: relative;
    display: table-cell;
    vertical-align: middle;
    color: #fff;
    z-index: 1;
  }

  div.server {
    width: 600px;
    display: table-cell;
    padding-right: 15pt;
    vertical-align: middle;
    color: #fff;
    text-align: right;
    > span {
      &:first-child {
        margin-left: 0;
      }
      display: inline-block;
      margin-left: 5pc;
      vertical-align: top;
      text-align: center;
    }
    em.value {
      display: block;
      margin-top: 9pt;
      margin-bottom: 3px;
      font-size: 18px;
    }
  }

}

div.shop-foods {
  width: 1000px;
  margin: 0 auto;
  div.foods-container {
    width: 75%;
    float: left;
  }
  div.billboard {
    width: 23.5%;
    float: right;
    margin-top: 60px;
    div.container {
      margin-bottom: 20px;
      border-radius: 2px 2px 0 0;
      background-color: #fff;
      box-shadow: 0 1px 1px rgba(0,0,0,.12);
      h3 {
        margin-bottom: 1em;
        padding: 0 1em;
        line-height: 2.8em;
        background-color: #0089dc;
        color: #fff;
      }
      p {
        padding: 0 15px 20px;
        line-height: 2;
        margin-bottom: 20px;
        border-bottom: 1px dashed #ccc;
      }
    }
  }
  h2 {
    padding: 20px 0 10px 15px;
    font-size: 20px;
  }
  div.food {
    display: table;
    width: 100%;
    padding: 15px 0;
    text-align: center;
    margin-bottom: 9pt;
    font-size: 9pt;
    background-color: #fff;
    border: 1px solid #eee;
    height: 102px;

    > div {
      display: table-cell;
      vertical-align: middle;
    }
  }
  div.image {
     width: 10%;
     img {
       width: 4pc;
       height: 4pc;
     }
  }
  div.intro {
    width: 60%;
    text-align: left;
    max-width: 0;
    h3 {
      font-size: 14px;
      font-weight: 700;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
    P.content {
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      color: #999;
    }
  }
  div.price {
    width: 12%;
    color: #333;
    > span {
      font-size: 9pt;
      color: #999;
      margin-right: 3px;
    }
  }
  div.add-to-cart {
    width: 15%;

    button {
      display: inline-block;
      background-color: #0089dc;
      color: #fff;
      border: 0;
      cursor: pointer;
      width: 90px;
      height: 26px;
      line-height: 26px;
      border-radius: 20px;
      text-align: center;
      outline: 0;
    }
  }
}
</style>

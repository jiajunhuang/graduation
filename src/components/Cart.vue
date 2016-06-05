<template>
  <div class="fixed-navbar" v-on:click.stop >
    <div class="control">
      <div class="order">
        <a class="item" v-link="{  path: '/order' }"><i class="fa fa-list"></i></a>
        <span class="tips">我的订单</span>
      </div>
      <div class="shopping-cart" v-bind:class="{ 'has-food': sumNum !== 0 }">
        <a href="#"  v-on:click.prevent="toggleNavbarContent()" class="item"
            v-bind:class="{'focus': isShowNavbarContent === true}">
          <i class="foods-sum-number" v-text="sumNum"></i>
          <i class="fa fa-shopping-cart"></i> 购物车</a>
      </div>
    </div>
    <div class="content" v-bind:class="{ show: isShowNavbarContent === true}">
      <div class="title clearfix"><h4>购物车</h4><a href="#" v-on:click.prevent="toggleNavbarContent()">>></a></div>
      <div class="no-list" v-show="sumNum === 0">
        <i class="fa fa-clock-o"></i>
        <p>购物车空空如也</p>
        <p>快去订餐吧，总有你心仪的美食</p>
      </div>
      <div class="has-list" v-show="sumNum !== 0">
        <dt class="clearfix"><a v-on:click.prevent="deleteAll()">[清空]</a></dt>
        <ul>
          <li class="clearfix" v-for="food in foods" track-by="$index">
            <div class="name" v-text="food.name"></div>
            <div class="quantity">
              <span v-on:click="minusFoodQuantity(food)">-</span>
              <input v-model="food.quantity">
              <span v-on:click="plusFoodQuantity(food)">+</span>
            </div>
            <div class="price" v-text="'￥'+ (food.price * food.quantity)"></div>
          </li>
        </ul>
      </div>
      <div class="summary" v-show="sumNum !== 0">
        <p>共<span> {{ sumNum }} </span>份，总计<span> {{ sumPrice }} </span>元</p>
        <button>去结算</button>
      </div>
    </div>
    <div class="back-to-top" v-bind:class="{'focus': isShowBackToTop === true}">
      <a href="#" class="item" v-on:click.prevent="backToTop()" ><i class="fa fa-arrow-up"></i></a>
      <span class="tips">返回顶部</span>
    </div>
  </div>
</template>

<script>
import { cartFoods } from '../vuex/getters'
import { deleteAll,
         plusFoodQuantity,
         minusFoodQuantity
          } from '../vuex/actions'
export default {
  name: 'Cart',
  created() {
    window.addEventListener('click', this.clickHandler)
    window.addEventListener('keyup', this.escHandler)
    window.addEventListener('scroll', this.scrollHandler)
  },
  data() {
    return {
      isShowNavbarContent: false,
      scrollEventTimer: null,
      isShowBackToTop: false,
      sumPrice: 0,
      sumNum: 0,
      foods: []
    }
  },
  methods: {
    toggleNavbarContent() {
      this.isShowNavbarContent = !this.isShowNavbarContent
    },
    hideNavbar() {
      this.isShowNavbarContent = false
    },
    escHandler(event) {
      event.keyCode === 27 && this.hideNavbar()
    },
    clickHandler() {
      this.hideNavbar()
    },
    scrollHandler() {
      clearTimeout(this.scrollEventTimer)
      this.scrollEventTimer = setTimeout(() => {
        this.isShowBackToTop = !!((document.body.scrollTop || document.documentElement.scrollTop) > 1500)
      }, 500)
    },
    backToTop() {
      window.scrollTo(0, 0)
    }
  },
  beforeDestory() {
    window.removeEventListener('click', this.clickHandler)
    window.removeEventListener('keyup', this.escHandler)
  },
  watch: {
    cartFoods: {
      handler(value) {
        this.foods = []
        this.foods = value.foods
        this.sumPrice = value.sumPrice
        this.sumNum = value.sumNum
        return value
      }
    }
  },
  ready() {
    // fix watch dont trigger when router change
    this.foods = this.cartFoods.foods
    this.sumPrice = this.cartFoods.sumPrice
    this.sumNum = this.cartFoods.sumNum
  },
  vuex: {
    getters: {
      cartFoods
    },
    actions: {
      deleteAll,
      plusFoodQuantity,
      minusFoodQuantity
    }
  }
}
</script>

<style lang='sass' scoped>

$height: 200px;
$bgColor: #504d53;
$fontColor: #ccc;
%line {
  content: ' ';
  display: inline-block;
  position: absolute;
  left: 8px;
  height: 1px;
  width: 19px;
  background-color: #737074;
}
%tips {
  position: absolute;

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


div.fixed-navbar {
  z-index: 99;
  position: fixed;
  right: 0px;
  top: 0px;
  bottom: 0px;
  width: auto;
  height: 100%;
  display: inline-block;
  background-color: $bgColor;

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

    &:hover,
    &.focus {
      background-color: #26a2ff;
      color: #fff;
      outline: 0;
    }
    &.has-food {
      margin-top: 32px;
    }
  }

  div.control {
    height: $height;
    width: 35px;
    position: absolute;
    top: 50%;
    margin-top: -$height * 0.5;

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
      &:before {
        @extend %line;
        top: -4px;
      }
      i {
        font-size: 20px;
      }
    }

    div.shopping-cart {
      position: relative;
      &:before {
        @extend %line;
        top: -4px;
      }
      &:after {
        @extend %line;
        bottom: -4px;
      }
      &.has-food {
        margin-top: 32px;
        &:before {
          top: -34px;
        }
        i.foods-sum-number {
          display: block;
        }
      }
      i {
        margin-bottom: 4px;
        font-size: 20px;
      }
      i.foods-sum-number {
        display: none;
        font-size: 12px;
        width: 22px;
        height: 20px;
        line-height: 20px;
        border-radius: 3px;
        color: #fff;
        background-color: #f63;
        top: -28px;
        left: 0;
        right: 0;
        margin: auto;
        position: absolute;
        font-weight: 700;
        font-style: normal;
        &:after {
          left: 0;
          right: 0;
          margin: auto;
          position: absolute;
          border: 6px solid;
          border-color: #f63 transparent transparent;
          width: 0;
          height: 0;
          bottom: -11px;
          content: '';
        }
      }
    }
    span.tips {
      @extend %tips;
      right: 50px;
      top: 2px;
      width: 5em;
    }
  }

  div.content {
    width: 0px;
    height: 100%;
    margin-left: 35px;
    background-color: #E6E6E6;
    overflow: hidden;
    transition: all 0.1s ease-in;
    &.show {
      width: 295px;
    }
    div.title {
      width: 295px;
      background: #fff;
      font-size: 16px;
      color: #999;
      padding: 5px 10px;
      margin-bottom: 10px;
      border-bottom: 1px solid #ddd;
      h4 {
        float: left;
        color: #333;
      }
      a {
        float: right;
        text-decoration: none;
      }
    }
    div.no-list {
      text-align: center;
      i.fa-clock-o {
        margin-top: 40px;
        font-size: 60px;
      }
      p:nth-child(2) {
        margin-top: 10px;
        font-weight: 400;
        font-size: 18px;
      }
      p:nth-child(3) {
        color: #999;
        font-size: 12px;
      }

    }
    div.has-list {
      padding: 10px;
      background-color: #fff;
      border: solid #ddd;
      border-width: 1px 0;
      margin-bottom: 10px;
      dt {
        font-size: 12px;
        border-bottom: 1px solid #ddd;
        padding: 2px 3px;
        color: #666;
        a {
          float: right;
          color: #0089dc;
          font-size: 12px;
          cursor: pointer;
        }
      }
      ul {
        li {
          margin: 5px 0;
          padding: 5px 10px;
          font-size: 12px;
          line-height: 20px;
          color: #666;
          &:hover {
            background-color: #f9f9f9;
            div.quantity {
              span {
                visibility: visible;
                opacity: 1;
              }
            }
          }
          div.name {
            float: left;
            width: 45%;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
          }
          div.quantity {
            float: left;
            width: 26%;
            span {
              transition: opacity .2s ease,visibility .2s ease;
              opacity: 0;
              visibility: hidden;
              user-select: none;
              background: #f5f5f5;
              color: #999;
              vertical-align: bottom;
              font-size: 12px;
              line-height: 18px;
              cursor: pointer;
              float: left;
              display: inline-block;
              width: 20px;
              height: 20px;
              text-align: center;
              border: 1px solid #ddd;
              &:first-child {
                border-right: none;
              }
              &:hover {
                color: #2a89cc;
              }
            }
            input {
              float: left;
              display: inline-block;
              width: 20px;
              height: 20px;
              text-align: center;
              border: 1px solid #ddd;
              font-size: 12px;
              color: #666;
              &+span {
                border-left: none;
              }
            }
          }
          div.price {
            font-weight: 700;
            float: right;
            color: #f17530;
          }
        }
      }
    }
    div.summary {
      padding: 20px 10px;
      text-align: right;
      border-top: 1px solid #ddd;
      width: 295px;
      left: 35px;
      bottom: 0;
      background: #fff;
      opacity: .95;
      position: absolute;
      p {
        font-size: 14px;
        text-align: right;
        span {
          color: #f74342;
        }
      }
      button {
        display: block;
        border: 0;
        margin-top: 10px;
        line-height: 32px;
        width: 100%;
        text-align: center;
        background: #fa5858;
        color: #fff;
      }

    }
  }
  div.back-to-top {
    position: relative;
    bottom: 80px;
    width: 35px;
    display: none;
    &.focus {
      display: inline-block;
    }
    &:before {
      @extend %line;
      top: -4px;
    }
    &:after {
      @extend %line;
      bottom: -4px;
    }
    &:hover {
      .tips {
        display: block;
      }
    }
    i {
      font-size: 20px;
    }
    span.tips {
      @extend %tips;
      display: none;
      right: 50px;
      top: 2px;
      width: 5em;
    }
  }
}
</style>

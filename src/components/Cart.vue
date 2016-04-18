<template>
  <div class="fixed-navbar" v-on:click.stop>
    <div class="control">
      <div class="order">
        <a class="item" v-link="{  path: 'order' }"><i class="fa fa-list"></i></a>
        <span class="tips">我的订单</span>
      </div>
      <div class="shopping-cart">
        <a href="#"  v-on:click.prevent="toggleNavbarContent()" class="item" v-bind:class="{'focus': isShowNavbarContent === true}">
          <i class="fa fa-shopping-cart"></i> 购物车</a>
      </div>
    </div>
    <div class="content" v-bind:class="{ show: isShowNavbarContent === true}">
      <div class="title clearfix"><h4>购物车</h4><a href="#" v-on:click.prevent="toggleNavbarContent()">>></a></div>
      <div class="no-list">
        <i class="fa fa-bell"></i>
        <p>购物车空空如也</p>
        <p>快去订餐吧，总有你心仪的美食</p>
      </div>
      <div class="list">
        <a href="#" v-for="food in cartFoods" track-by="$index">{{ food.name }}</a>
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
console.log(cartFoods)
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
      isShowBackToTop: false
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
  vuex: {
    getters: {
      cartFoods
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
      i {
        margin-bottom: 4px;
        font-size: 20px;
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
      i.fa-bell {
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

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
      <!-- <div class="list">

      </div> -->

    </div>
  </div>
</template>

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

  div.control {
    height: $height;
    width: 35px;
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

      &:hover,
      &.focus {
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
      position: absolute;
      right: 50px;
      top: 2px;
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

  div.content {
    width: 0px;
    height: 100%;
    margin-left: 35px;
    background-color: #E6E6E6;
    overflow: hidden;
    transition: all 5.5s ease-out-in;
    &.show {
      width: 295px;
    }
    div.title {
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
}
</style>

<script>
export default {
  name: 'FixedNavbar',
  created() {
    window.addEventListener('click', this.clickHandler)
    window.addEventListener('keyup', this.escHandler)
  },
  data() {
    return {
      isShowNavbarContent: false
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
    }
  }
}
</script>

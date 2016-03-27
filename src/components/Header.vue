<template>
  <header>
    <div class="container clearfix">
      <h1><a v-link="{ path: '/index' , exact: true}" class="logo"><span>吃了么在线订餐</span><img src="../assets/logo.png" alt="吃了么在线订餐" /></a></h1>
      <div class="navbar clearfix">
        <a class="home" v-link="{ path: '/index' }">首页</a>
        <a v-link="{ path: '/shop' }">品牌商家</a>
        <a v-link="{ path: '/order' }">我的订单</a>
      </div>
      <div class="user">
        <a herf="#" class="user-name" v-on:click.prevent="toggleDropDown()">JiajunHuang</a>
        <!-- <a class="user-login" v-link="{ path: '/login' }">登陆 / 注册</a> -->
        <div class="user-items" v-bind:class="{ show: isShowDropDown}">
          <a v-link="{ path: '/ssettings' }">个人中心</a>
          <a v-link="{ path: '/security' }">安全设置</a>
          <a v-link="{ path: '/layout' }">退出登录</a>
        </div>
      </div>
    </div>
  </header>
</template>

<style lang='sass' scoped>
header {
  background-color: #1e89e0;

  height: 60px;
  div.container {
    width: 1000px;
    margin: 0 auto;
  }
  h1 {
    float: left;

    span {
      display: block;
      height: 0;
      overflow: hidden;
      text-indent: -900em;
    }
    a {
      display: inline-block;
      height: 60px;
      padding: 15px 0px;
      line-height: 0px;
      font-size: 26px;
    }
    img {
      height: 100%;
    }
  }

  div.navbar {
    float: left;
    margin-left: 30px;
    a {
      float: left;
      color: white;
      text-decoration: none;
      display: inline-block;
      height: 60px;
      line-height: 60px;
      width: 112px;
      text-align: center;

      &:hover {
        background-color: #0c77d1;
      }
      &.v-link-active {
        background-color: #006bc7;
      }
    }
  }

  div.user {
    float: right;
    display: inline-block;
    position: relative;
    border-radius: 2px;
    margin-right: 35px;
    a.user-name {
      color: white;
      text-decoration: none;
      cursor: pointer;
      line-height: 60px;
      &.user-name {
        font-weight: lighter;
      }

      &.user-login {

      }
    }

    .user-items {
      &.show {
        display: inline-block;
      }
      &:before {
        content: ' ';
        border: 5px solid #fff;
        display: block;
        position: absolute;
        top: -10px;
        border-color: transparent transparent #fff;
        right: 58px;
      }
      background-color: #FFF;
      display: none;
      position: absolute;
      top: 50px;
      left: -20px;
      width: 122px;
      padding: 4px 6px;
      box-shadow: 0 1px 2px rgba(0,0,0,.5);
      a {
        color: #999;
        line-height: 32px;
        text-align: center;
        display: block;
        text-decoration: none;
        &:hover {
          background-color: #f1f1f1;
        }
        &:last-child {
          border-top: 1px solid #eee;
        }
      }
    }
  }
}
</style>

<script>
export default {
  name: 'TopHeader',
  data() {
    return {
      isShowDropDown: false
    }
  },
  methods: {
    toggleDropDown() {
      this.isShowDropDown = !this.isShowDropDown
    }
  }
}
</script>

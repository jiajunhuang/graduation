<template>
  <header v-bind:class="{ shop: $route.shop === true }">
    <div class="container clearfix">
      <h1><a v-link="{ path: '/index' }" class="logo"><span>吃了么在线订餐</span><img src="../assets/logo.png" alt="吃了么在线订餐" /></a></h1>
      <div class="navbar clearfix">
        <a v-link="{ path: '/index' }" class="home">首页</a>
        <a v-link="{ path: $route.path }" v-show="$route.shop === true">商家</a>
        <a v-link="{ path: '/order' }">我的订单</a>
      </div>
      <div class="user">
        <a v-show="isLogin === false" class="user-login" v-link="{ path: '/user_login' }">登陆 / 注册</a>
        <div class="is-login" v-show="isLogin === true">
          <a herf="#" class="user-name" v-on:click.prevent="toggleDropDown()">{{ userName }}</a>
          <div class="user-items" v-bind:class="{ show: isShowDropDown}">
            <a v-link="{ path: '/settings'}"><i class="fa fa-user"></i> 个人中心</a>
            <a v-link="{ path: '/security'}"><i class="fa fa-asterisk"></i> 安全设置</a>
            <a ><i class="fa fa-power-off"></i> 退出登录</a>
          </div>
        </div>
        
      </div>
    </div>
  </header>
</template>

<style lang='sass'>
header {
  background-color: #1e89e0;
  height: 60px;

  &.shop {
    position: absolute;
    width: 100%;
    height: 3pc;
    background-color: rgba(0,0,0,.4);
    h1 {
      height: 3pc;
      a {
        line-height: inherit;
        font-size: 2pc;
        height: 40px;
        padding: 5px 0px;
      }
    }
    div.navbar {
      a {
        line-height: 3pc;
        height: 3pc;
        &.v-link-active,
        &:hover {
          background-color: rgba(0,0,0,.1) !important;
        }
      }
    }
    div.user {
      a.user-name {
        line-height: 3pc;
      }
    }

  }

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
    a {
      color: white;
      text-decoration: none;
      cursor: pointer;
      line-height: 60px;
      font-weight: lighter;

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
        right: 10px;
      }
      background-color: #FFF;
      display: none;
      position: absolute;
      top: 50px;
      right: 0px;
      width: 122px;
      padding: 4px 6px;
      box-shadow: 0 1px 2px rgba(0,0,0,.5);
      z-index: 99;
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
  ready() {
    this.$http.get(
      '/login/status'
    ).then((response) => {
      let data = response.data
      if (data.status === 1) {
        return undefined
      }
      if (data.status === 0) {
        return data.uid
      }
    }, (err) => {
      console.log(err)
    }).then(uid => {
      if (uid === undefined) return false
      this.$http.get('/user/' + uid)
        .then(response => {
          let data = response.data
          this.isLogin = true
          this.userName = data.name
        })
    })
  },
  data() {
    return {
      isShowDropDown: false,
      userName: '',
      isLogin: false
    }
  },
  methods: {
    toggleDropDown() {
      this.isShowDropDown = !this.isShowDropDown
    }
  }
}
</script>

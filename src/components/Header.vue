
<template>
  <header>
    <div class="container clearfix">
      <h1><a href="#/" class="logo"><span>在线订餐</span></a></h1>
      <a class="home" href="#/">首页</a>
      <div class="user">
        <a href="#/user-name">test</a>
        <div class="user-item">
          <a href="#/settings">个人中心</a>
          <a href="#/security">安全设置</a>
          <a href="#/layout">退出登录</a>
        </div>
      </div>
    </div>
  </header>
</template>

<style lang='sass' scoped>
header {
  background-color: #1e89e0;
  div.container {
    width: 1000px;
    margin: 0 auto;
    /*background-color: red;*/
  }
  h1 {
    float: left;
    span {
      display: block;
      height: 0;
      overflow: hidden;
      text-indent: -900em;
    }
  }
  a {
    color: white;
  }
  div.user {
    float: rigth;
  }
}
</style>

<script>
export default {
  name: 'TopHeader'
}
</script>

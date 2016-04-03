<template >
<div class="shop-items-container clearfix">
  <a class="item">
    <div class="logo">
      <img src="//fuss10.elemecdn.com/0/3f/2a2d3d9f89dd24ba16335151f8d7ajpeg.jpeg?imageMogr2/thumbnail/70x70/format/webp/quality/85" alt="" width="70" height="70"/>
      <span class="speed">45+ 分钟</span>
    </div>
    <div class="content">
      <h4>云膳麻辣（上海）</h4>
      <p class="grade slice">⭐️⭐️⭐️⭐️</p>
      <p class="count slice">月售712单</p>
      <p class="spend slice">0元起送</p>
    </div>
  </a>
</div>
</template>

<style lang="sass">

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
  &:hover {
    background-color: #f5f5f5;
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
    name: 'IndexShopItem'
  }
</script>

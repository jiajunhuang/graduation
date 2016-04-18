<template >
  <div id="excavator" v-on:click.stop>
    <div class="filter">
      <span class="category">商家分类：</span>
      <div class="contents clearfix">
        <a href="" class="focus">全部商家</a>
        <a href="" class="hot">品牌商家</a>
        <a href="">快餐类</a>
        <a href="">正餐类</a>
        <a href="">小零食</a>
      </div>
    </div>
    <div class="control clearfix">
      <div class="sort clearfix">
        <a href="#" class="focus">默认排序</a>
        <a href="#" >销量好</a>
        <a href="#">评价好</a>
        <a href="#">
          <span>其他排序</span>
          <div class="others">

          </div>
        </a>
        <a href="#">起送价格</a>
      </div>
      <div class="option clearfix">
        <label ><input type="checkbox"> 新开商家</label>
        <label ><input type="checkbox"> 免费配送</label>
        <label ><input type="checkbox"> 可开发票</label>
      </div>
    </div>
  </div>
</template>

<style lang="sass" scoped>
  #excavator {
    width: 1000px;
    margin: 0 auto;
    background-color: #fff;
    border: 1px solid #e6e6e6;
    font-size: 14px;
  }
  div.filter {
    padding: 10px 10px;

    span.category {
      float: left;
      color: #999;
      padding: 0 10px;
      margin-right: 8px;
      line-height: 34px;
    }
    .contents {
      a {
        float: left;
        padding: 0px 10px;
        line-height: 26px;
        border-radius: 3px;
        white-space: nowrap;
        display: inline-block;
        margin: 5px 6px;
        text-decoration: none;
        color: #666;
        &:hover {
          background-color: #f6f6f6;
        }
        &.focus {
          color: #FFF;
          background-color: #0089dc;
        }
        &.hot {
          color: #f74342;
        }
      }
    }
  }
  div.control {
    background-color: #f5f5f5;
    line-height: 40px;

    div.sort {
      float: left;
      margin-left: 10px;
      a {
        text-decoration: none;
        color: #666;
        padding: 0 7px;
        float: left;
        &.focus {
          color: #0089dc;
        }
      }
    }
    div.option {
      float: right;
      margin-right: 15px;
      position: relative;
      label {
        margin-left: 10px;
      }
      &:before {
        content: ' ';
        display: inline-block;
        position: absolute;
        width: 1px;
        height: 30px;
        background-color: #e6e6e6;
        top: 6px;
        left: -15px;
      }
    }
  }
</style>

<script>
  export default {
    name: 'Excavator',
    vuex: {
      getters: {
        count: state => state.count
      }
    }
  }
</script>

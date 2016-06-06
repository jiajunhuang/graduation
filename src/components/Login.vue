<template>
  <div class="container">
    <h3>登录</h3>
    <div class="login-form">
      <div class="form-group">
        <input class="account-input" type="text" placeholder="手机号" 
          v-model="phone">
      </div>
      <div class="form-group">
        <input v-model="passwd" class="account-input" type="password" placeholder="密码" >
      </div>
      <div class="form-group">
        <button class="account-btn submit" ng-class="{disabled: submitting}" 
          v-on:click="userLogin()">登录</button>
      </div>
    </div>
    <div class="account-line">
      <a v-link="{ path: '/register' }">新用户注册</a>
    </div>
  </div>
</template>

<script>
import { getUserInfo } from '../utils/api'
import { setUname, setUid } from '../vuex/actions'
export default {
  name: 'Login',
  data() {
    return {
      passwd: '',
      phone: ''
    }
  },
  methods: {
    userLogin() {
      if (this.phone === '') {
        window.alert('请输入手机号！')
        return false
      }
      if (this.passwd === '') {
        window.alert('请输入密码！')
        return false
      }
      this.$http.post(
        '/login/', {
          phone: this.phone,
          passwd: this.passwd
        }
      ).then((response) => {
        let data = response.data
        let hashArray = window.location.hash.split('#!')
        let previous = hashArray.length > 2 ? hashArray[hashArray.length - 1] : false

        if (data.status === 1) {
          window.alert('请填写正确的手机号和密码！')
          return false
        }
        if (data.status === 0) {
          let uid = data.sid.split(';')[1]
          console.log(previous)
          if (previous === false) {
            window.location = '/'
          } else {
            getUserInfo(uid).then((data) => {
              if (data.status === 1) {
                alert('登录失败')
                return false
              }
              if (data.status === 0) {
                this.setUname(data.name)
                this.setUid(data.uid)
              }
            }).then(() => {
              this.$route.router.go(previous)
            })
          }
        }
      }, (err) => {
        console.log(err)
      })
    }
  },
  vuex: {
    actions: {
      setUname,
      setUid
    }
  }
}
</script>

<style lang='sass' scoped>
  div.container {
    min-height: 280px;
    width: 340px;
    margin: 0 auto;
    margin-top: 100px;
    background-color: #fafcfe;
    border: 1px solid #dfe8f2;
    padding: 30px;
  }
  h3 {
    border-bottom: 2px solid #f4f4f4;
    padding: 0 20px 11px;
    font-size: 18px;
    font-weight: 700;
  }
  input.account-input {
    border: 1px solid #d3e1f1;
    border-radius: 2px;
    font-size: 14px;
    padding: 10px;
    height: 40px;
    width: 100%;
  }
  div.form-group {
    margin: 12px 0 10px;
  }
  button.account-btn {
    height: 40px;
    width: 100%;
    margin: 20px 0 0;
    display: block;
    border: 1px solid #3199e8;
    font-size: 16px;
    font-weight: 400;
    background: #3199e8;
    color: #fff;
    border-radius: 3px;
    cursor: pointer;
  }
  div.account-line {
    a {
      color: #07d;
      text-decoration: none;
    }
  }
</style>

/* global describe, it, expect */


import Vue from 'vue'
import Header from '../../src/components/Header.vue'

describe('Header.vue', function () {
  // asserting JavaScript options
  it('show have correct name', function () {
    expect(Header.name).toBe('TopHeader')
  })

  it('should have correct default data', function () {
    expect(Header.data().isShowDropDown).toBe(false)
  })

  // it('')


  // asserting rendered result by actually rendering the component
  // it('should render correct message', function () {
  //   var vm = new Vue({
  //     template: '<div><test></test></div>',
  //     components: {
  //       test: Header
  //     }
  //   }).$mount()
  //   expect(vm.$el.querySelector('h2.red').textContent).toBe('Hello from Component A!')
  // })
})

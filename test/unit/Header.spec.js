/* global describe, it, expect */

import Vue from 'vue'
import Header from '../../src/components/Header.vue'

describe('Header.vue', function () {

  it('should have correct name', function () {
    expect(Header.name).toBe('TopHeader')
  })

  it('should have correct default data', function () {
    expect(Header.data().isShowDropDown).toBe(false)
    expect(Header.data().focusItem).toBe(0)
  })


  var vm = new Vue({
    template: '<div><test></test></div>',
    components: {
      test: Header
    }
  }).$mount()

  it('should be Vue instance', function () {
    expect(vm instanceof Vue).toBe(true)
  })

  it('should have correct switchItem function', function () {
    expect(typeof Header.methods.toggleDropDown).toBe('function')
    expect(vm.isShowDropDown).toBe(false)
    // Header.methods.toggleDropDown()
    // console.log(Header.data().isShowDropDown)
    // expect(Header.data().isShowDropDown).toBe(true)
    // Header.methods.toggleDropDown()
    // expect(Header.data().isShowDropDown).toBe(false)
  })


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

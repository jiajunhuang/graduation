export const cartFoods = state => {
  return {
    foods: state.cart.foods,
    sumNum: state.cart.num
  }
}

export const indexShops = state => {
  return state.excavator.shops
}

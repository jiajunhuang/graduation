export const cartFoods = state => {
  return {
    foods: state.cart.foods,
    sum: state.cart.sum
  }
}

export const indexShops = state => {
  return state.excavator.shops
}

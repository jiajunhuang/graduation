export const cartFoods = state => {
  return {
    foods: state.cart.foods,
    length: state.cart.sum
  }
}

export const foodsSumNumber = state => (state.cart.sum)

export const indexShops = state => {
  return state.excavator.shops
}

export const cartFoods = state => {
  return {
    foods: state.cart.foods,
    sumNum: state.cart.num,
    sumPrice: state.cart.foods.reduce((previous, current) => (
      previous + current.price * current.quantity
    ), 0)
  }
}

export const indexShops = state => {
  return state.excavator.shops
}

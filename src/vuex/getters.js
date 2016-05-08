export const cartFoods = state => (
  state.cart.foods.map(({ name, quantity, price }) => ({ name, quantity, price }))
)

export const foodsSumNumber = state => (state.cart.sum)

export const indexShops = state => {
  return state.excavator.shops
}

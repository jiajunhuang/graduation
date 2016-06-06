export const getUserInfo = uid => {
  return fetch('/user/' + uid)
    .then(response => response.json())
}

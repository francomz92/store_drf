import { getCart } from "../apis/cart.js"

export const initVisibilityChangeEvent = (userData) => {

    document.addEventListener('visibilitychange', async e => {
        e.preventDefault()
        await getCart(userData)
    })
}
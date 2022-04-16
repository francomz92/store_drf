import { addItemToCart } from '../apis/setCartItem.js';
import { getCart } from '../apis/getCart.js';

export const initCardClickEvent = ({ nodeListening, ProductData, userData, cart }) => {
   nodeListening.querySelectorAll('article').forEach((article) => {
      article.addEventListener('click', async (e) => {
         e.preventDefault();
         e.stopPropagation();

         const item = {
            product: ProductData.results.find((element) => +element.id === +article.id),
            ammount: 1,
         };

         await addItemToCart(userData, item);
         cart = await getCart(userData);
         document.querySelector('#cart').textContent = cart.results.items.length;
      });
   });
};

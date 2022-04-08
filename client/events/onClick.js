import { addItemToCart } from '../apis/setCartItem.js';

export const initCardClickEvent = ({ nodeListening, ProductData, userData }) => {
   nodeListening.querySelectorAll('article').forEach((article) => {
      article.addEventListener('click', (e) => {
         e.preventDefault();
         e.stopPropagation();
         const item = {
            product: ProductData.results.find((element) => +element.id === +article.id),
            ammount: 1,
         };
         addItemToCart(userData, item);
      });
   });
};

import { card } from '../components/Card.js';
import { getProductsData } from '../apis/getProducts.js';
import { setLinkStyles } from './setLinkStyle.js';

export const printProductCards = async () => {
   const $grid = document.getElementById('card-grid');
   const data = await getProductsData();
   if (data.results.length > 0) {
      setLinkStyles('./assets/styles/card.css');
      data.results.forEach((product) => {
         $grid.appendChild(card(product));
      });
   }
   return { $grid, data };
};

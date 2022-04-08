import { card } from '../components/Card.js';
import { setLinkStyles } from './setLinkStyle.js';

export const printProductCards = (productData) => {
   const $grid = document.getElementById('card-grid');

   setLinkStyles('./assets/styles/card.css');
   // Set product card
   if (productData.results.length > 0) {
      productData.results.forEach((product) => $grid.appendChild(card(product)));
   } else {
      $grid.innerHTML = '<h3 class="card-grid-empty">There are no products to display</h3>';
   }
   return { $grid, productData };
};

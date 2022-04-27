import { getProductsData } from '../../apis/products.js';
import { card } from '../../components/ProductCard.js';

export const printProductCards = async (sectionNode, filters) => {
   const productData = await getProductsData(filters);
   let $grid = sectionNode.querySelector('#card-grid') || document.createElement('div');

   $grid.innerHTML = '';
   $grid.classList.add('foot-layout');
   $grid.setAttribute('id', 'card-grid');

   // Set product card
   if (productData.results.length > 0) {
      productData.results.forEach((product) => $grid.appendChild(card(product)));
   } else {
      $grid.innerHTML = '<h3 class="card-grid-empty">There are no products to display</h3>';
   }

   return { $grid, productData };
};

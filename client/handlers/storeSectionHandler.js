import { getProductsData } from '../apis/getProducts.js';
import { setLinkStyles } from '../helpers/setLinkStyle.js';
import { printStoreAsideContent } from '../helpers/printStoreAsideContent.js';
import { printProductCards } from '../helpers/printProductCards.js';
import { setCartItem } from '../apis/setCartItem.js';

export const storeSectionHandler = async (userData) => {
   setLinkStyles('../assets/styles/section.store.css');

   const $aside = await printStoreAsideContent();
   // const $selectFilter = $aside.querySelector('select[name=category]');
   const productsResponse = await getProductsData();
   const { $grid, data } = printProductCards(productsResponse);

   if (userData) {
      $grid.querySelectorAll('article').forEach((article) => {
         article.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const item = {
               product: data.results.find((element) => +element.id === +article.id),
               ammount: 1,
            };
            setCartItem(userData, item);
         });
      });
   }

   $aside.addEventListener('change', async (e) => {
      e.preventDefault();
      if (e.target.matches('select[name=category]')) {
         const productsResponse = await getProductsData({ category__name: e.target.value });
         document.getElementById('card-grid').innerHTML = '';
         printProductCards(productsResponse);
      }
   });
};

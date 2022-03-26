import { setLinkStyles } from '../helpers/setLinkStyle.js';
import { printStoreAsideContent } from '../helpers/printStoreAsideContent.js';
import { printProductCards } from '../helpers/printProductCards.js';
import { setCartItem } from '../apis/setCartItem.js';

export const storeSectionHandler = async (userData) => {
   setLinkStyles('../assets/styles/section.store.css');
   printStoreAsideContent();
   const { $grid, data } = await printProductCards();

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
};

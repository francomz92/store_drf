import { getProductsData } from '../apis/getProducts.js';
import { setLinkStyles } from '../helpers/setLinkStyle.js';
import { printStoreAsideContent } from '../helpers/printStoreAsideContent.js';
import { printProductCards } from '../helpers/printProductCards.js';
import { initCardClickEvent } from '../events/onClick.js';
import { initStoreSectionChangeEvent } from '../events/onChange.js';
import { printProductOrderingSelect } from '../helpers/printProductOrderingFilter.js';

export const storeSectionHandler = async (userData, cart) => {
   setLinkStyles('../assets/styles/section.store.css');

   const $aside = await printStoreAsideContent();
   const productsResponse = await getProductsData();
   const { $grid, productData } = printProductCards(productsResponse);
   const $storeSection = document.querySelector('.store-section');

   printProductOrderingSelect($storeSection);
   if (userData) {
      initCardClickEvent({ nodeListening: $grid, ProductData: productData, userData: userData }, cart);
   }
   initStoreSectionChangeEvent({ nodeListening: $storeSection });
};

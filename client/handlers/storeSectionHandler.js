import { getProductsData } from '../apis/getProducts.js';
import { loadStyles } from '../helpers/linkStyle.js';
import { printStoreAsideContent } from '../helpers/storeAsideContent.js';
import { printProductCards } from '../helpers/productCards.js';
import { initCardClickEvent } from '../events/onClick.js';
import { initStoreSectionChangeEvent } from '../events/onChange.js';
import { printProductOrderingSelect } from '../helpers/productOrderingFilter.js';

export const storeSectionHandler = async (userData, cart) => {
   loadStyles('../assets/styles/section.store.css');

   const $storeSection = document.querySelector('.store-section');
   const $aside = await printStoreAsideContent();
   const productsResponse = await getProductsData();
   const { $grid, productData } = printProductCards(productsResponse);

   printProductOrderingSelect($storeSection);
   // Init events listener
   if (userData) {
      initCardClickEvent({ nodeListening: $grid, ProductData: productData, userData: userData }, cart);
   }
   initStoreSectionChangeEvent({ nodeListening: $storeSection });
};

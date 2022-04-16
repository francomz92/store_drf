import { printStoreAsideContent } from '../helpers/storeAsideContent.js';
import { printProductCards } from '../helpers/productCards.js';
import { initCardClickEvent } from '../events/onClick.js';
import { initStoreSectionChangeEvent } from '../events/onChange.js';
import { printProductOrderingSelect } from '../helpers/productOrderingFilter.js';
import { printProductSearchFilter } from '../helpers/productSearchFilter.js';
import { initStoreSectionKeyupEvent } from '../events/onKeyup.js';

const filters = {
   category__name: null,
   name: null,
   unit_price__gte: 0,
   unit_price__lte: null,
   offer: null,
   ordering: null,
   search: null,
};

export const storeSectionHandler = async (mainNode, userData, cart) => {
   const $storeSection = document.createElement('section');
   const $aside = await printStoreAsideContent();
   $storeSection.classList.add('store-section');
   $storeSection.appendChild($aside);
   const { $grid, productData } = await printProductCards($storeSection, filters);

   printProductSearchFilter($storeSection);
   printProductOrderingSelect($storeSection);
   $storeSection.appendChild($grid);
   mainNode.appendChild($storeSection);

   // Init events listener
   if (userData) {
      initCardClickEvent({
         nodeListening: $grid,
         ProductData: productData,
         userData: userData,
         cart: cart,
      });
   }
   initStoreSectionChangeEvent({ nodeListening: $storeSection, filters: filters });
   initStoreSectionKeyupEvent({ nodeListening: $storeSection, filters: filters });
};

import { printStoreAsideContent } from '../helpers/store/storeAsideContent.js';
import { printProductCards } from '../helpers/store/productCards.js';
import { initCardClickEvent, initStoreSectionclickEvent } from '../events/onClick.js';
import { initStoreSectionChangeEvent } from '../events/onChange.js';
import { printProductOrderingSelect } from '../helpers/store/productOrderingFilter.js';
import { printProductSearchFilter } from '../helpers/store/productSearchFilter.js';
import { initStoreSectionKeyupEvent } from '../events/onKeyup.js';
import { printPagination } from '../helpers/store/pagination.js';

const MAX_ITEMS_PER_PAGE = 10;

const filters = {
   category__name: null,
   name: null,
   unit_price__gte: 0,
   unit_price__lte: null,
   offer: null,
   ordering: null,
   search: null,
   page: 1,
   page_size: MAX_ITEMS_PER_PAGE,
};

export const storeSectionHandler = async (mainNode, userData, cart) => {
   const $storeSection = document.createElement('section');
   const $pagination = document.createElement('div');
   const $aside = await printStoreAsideContent();
   $storeSection.classList.add('store-section');
   $storeSection.appendChild($aside);
   $pagination.classList.add('pagination-container');
   const { $grid, productData } = await printProductCards($storeSection, filters);
   const quantityPages = Math.ceil(productData.count / MAX_ITEMS_PER_PAGE);

   printProductSearchFilter($storeSection);
   printProductOrderingSelect($storeSection);
   printPagination($pagination, quantityPages, filters);
   $storeSection.appendChild($grid);
   $storeSection.appendChild($pagination);
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

   initStoreSectionChangeEvent({
      nodeListening: $storeSection,
      filters: filters,
      itemsPerPage: MAX_ITEMS_PER_PAGE,
   });
   initStoreSectionKeyupEvent({
      nodeListening: $storeSection,
      filters: filters,
      itemsPerPage: MAX_ITEMS_PER_PAGE,
   });
   initStoreSectionclickEvent({
      nodeListening: $storeSection,
      filters: filters,
      itemsPerPage: MAX_ITEMS_PER_PAGE,
   });
};

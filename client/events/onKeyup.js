import { printPagination, setStyleCurrentPage } from '../helpers/store/pagination.js';
import { printProductCards } from '../helpers/store/productCards.js';

export const initStoreSectionKeyupEvent = ({ nodeListening, filters, itemsPerPage }) => {
   nodeListening.addEventListener('keyup', async (e) => {
      // Search filter
      if (e.target.matches('input[name=search]') && e.key === 'Enter') {
         filters['search'] = e.target.value;
      }

      const { productData } = await printProductCards(nodeListening, filters);
      const $paginationContainer = nodeListening.querySelector('.pagination-container');
      let quantityPages = Math.ceil(productData.count / itemsPerPage);
      printPagination($paginationContainer, quantityPages, filters);
      if (quantityPages > 0) {
         setStyleCurrentPage($paginationContainer.firstChild.querySelectorAll('span'), 1, 1, quantityPages);
      }
   });
};

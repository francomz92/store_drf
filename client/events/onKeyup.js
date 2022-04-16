import { printProductCards } from '../helpers/productCards.js';

export const initStoreSectionKeyupEvent = ({ nodeListening, filters }) => {
   nodeListening.addEventListener('keyup', async (e) => {
      // Search filter
      if (e.target.matches('input[name=search]') && e.key === 'Enter') {
         filters['search'] = e.target.value;
      }

      await printProductCards(nodeListening, filters);
   });
};

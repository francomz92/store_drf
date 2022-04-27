import { printProductCards } from '../helpers/store/productCards.js';

export const initStoreSectionChangeEvent = ({ nodeListening, filters }) => {
   nodeListening.addEventListener('change', async (e) => {
      e.preventDefault();
      // Aside category filter
      if (e.target.matches('select[name=category]')) filters['category__name'] = e.target.value;
      // Aside Offer checkbox
      if (e.target.matches('input[name=offer]')) {
         if (e.target.getAttribute('checked') !== 'true') {
            filters['offer'] = true;
            e.target.setAttribute('checked', true);
         } else {
            filters['offer'] = null;
            e.target.setAttribute('checked', false);
         }
      }
      // Product ordering by unit price
      if (e.target.matches('select[name=ordering]')) filters['ordering'] = e.target.value;
      // Aside range filter by unit price (less than or equal)
      if (e.target.matches('input[name=unit_price__lte]')) {
         filters['unit_price__lte'] = e.target.value;
         e.target.setAttribute('title', e.target.value);
         e.target.previousElementSibling.textContent = `Hasta: $${e.target.value}`;
      }
      // Aside range filter by unit price (greater than or equal)
      if (e.target.matches('input[name=unit_price__gte]')) {
         filters['unit_price__gte'] = e.target.value;
         e.target.setAttribute('title', e.target.value);
         e.target.previousElementSibling.textContent = `Desde: $${e.target.value}`;
      }

      await printProductCards(nodeListening, filters);
   });
};

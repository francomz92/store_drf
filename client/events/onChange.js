import { getProductsData } from '../apis/getProducts.js';
import { printProductCards } from '../helpers/printProductCards.js';

const filters = {
   category__name: null,
   name: null,
   unit_price__gte: 0,
   unit_price__lte: null,
   offer: null,
   ordering: null,
};

export const initStoreSectionChangeEvent = ({ nodeListening }) => {
   nodeListening.addEventListener('change', async (e) => {
      e.preventDefault();
      if (e.target.matches('select[name=category]')) filters['category__name'] = e.target.value;
      if (e.target.matches('input[name=offer]')) {
         if (e.target.getAttribute('checked') !== 'true') {
            filters['offer'] = true;
            e.target.setAttribute('checked', true);
         } else {
            filters['offer'] = null;
            e.target.setAttribute('checked', false);
         }
      }
      if (e.target.matches('select[name=ordering]')) filters['ordering'] = e.target.value;
      if (e.target.matches('input[name=unit_price__lte]')) {
         filters['unit_price__lte'] = e.target.value;
         e.target.setAttribute('title', e.target.value);
         e.target.previousElementSibling.textContent = `Hasta: $${e.target.value}`;
      }
      if (e.target.matches('input[name=unit_price__gte]')) {
         filters['unit_price__gte'] = e.target.value;
         e.target.setAttribute('title', e.target.value);
         e.target.previousElementSibling.textContent = `Desde: $${e.target.value}`;
      }

      const productsResponse = await getProductsData(filters);
      document.getElementById('card-grid').innerHTML = '';
      printProductCards(productsResponse);
   });
};

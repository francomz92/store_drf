import { searchFilter } from '../components/SearchFilter.js';

export const printProductSearchFilter = (nodeHTML) => {
   nodeHTML.appendChild(
      searchFilter({
         nameAttr: 'search',
         listId: 'searched-products',
         placeHolder: 'Search...',
         styles: ['input-search'],
      })
   );
};

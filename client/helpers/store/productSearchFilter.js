import { SearchFilter } from '../../components/SearchFilter.js';

export const printProductSearchFilter = (nodeHTML) => {
   nodeHTML.appendChild(
      SearchFilter({
         nameAttr: 'search',
         listId: 'searched-products',
         placeHolder: 'Search...',
         styles: ['input-search'],
      })
   );
};

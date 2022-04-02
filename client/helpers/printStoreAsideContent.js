import { setLinkStyles } from './setLinkStyle.js';
import { getCategories } from '../apis/getCategories.js';
import { selectFilter } from '../components/SelectFilter.js';
import { checkBoxFilter } from '../components/CheckBoxFilter.js';
import { filterContainer } from '../components/FilterContainer.js';

export const printStoreAsideContent = async () => {
   const $aside = document.querySelector('.store-aside');
   const categories = await getCategories();

   setLinkStyles('../assets/styles/aside.css');

   $aside.appendChild(
      filterContainer({
         labelName: 'Categoría:',
         labelReference: 'category',
         filter: selectFilter('category', categories),
      })
   );
   $aside.appendChild(
      filterContainer({ labelName: 'En oferta: ', labelReference: 'offer', filter: checkBoxFilter('offer') })
   );
   return $aside;
};

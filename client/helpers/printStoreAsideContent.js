import { setLinkStyles } from './setLinkStyle.js';
import { getCategories } from '../apis/getCategories.js';
import { selectFilter } from '../components/SelectFilter.js';
import { checkBoxFilter } from '../components/CheckBoxFilter.js';
import { filterContainer } from '../components/FilterContainer.js';
import { rangeFilter } from '../components/RangeFilter.js';

export const printStoreAsideContent = async () => {
   const $aside = document.querySelector('.store-aside');
   const categories = await getCategories();

   setLinkStyles('../assets/styles/aside.css');
   // SelectFilter for Categories
   $aside.appendChild(
      filterContainer({
         labelName: 'Categoría:',
         labelReference: 'category',
         filter: selectFilter({ nameAttr: 'category', objArray: categories, placeHolder: 'Todos' }),
      })
   );
   // CheckboxFilter for Offers
   $aside.appendChild(
      filterContainer({ labelName: 'En oferta: ', labelReference: 'offer', filter: checkBoxFilter('offer') })
   );
   $aside.appendChild(
      filterContainer({
         filter: rangeFilter('unit_price__gte', 'unit_price__lte'),
      })
   );

   return $aside;
};

import { getCategories } from '../../apis/categories.js';
import { SelectFilter } from '../../components/SelectFilter.js';
import { CheckBoxFilter } from '../../components/CheckBoxFilter.js';
import { FilterContainer } from '../../components/FilterContainer.js';
import { RangeFilter } from '../../components/RangeFilter.js';

export const printStoreAsideContent = async () => {
   const $aside = document.createElement('aside');
   const categories = await getCategories();

   $aside.classList.add('store-aside');
   // SelectFilter for Categories
   $aside.appendChild(
      FilterContainer({
         labelName: 'Categoría:',
         labelReference: 'category',
         filter: SelectFilter({ nameAttr: 'category', objArray: categories, placeHolder: 'Todos' }),
      })
   );
   // CheckboxFilter for Offers
   $aside.appendChild(
      FilterContainer({ labelName: 'En oferta: ', labelReference: 'offer', filter: CheckBoxFilter('offer') })
   );
   // RangeFilter for Unit Price
   $aside.appendChild(
      FilterContainer({
         filter: RangeFilter('unit_price__gte', 'unit_price__lte'),
      })
   );

   return $aside;
};

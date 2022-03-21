import { getCategories } from '../apis/getCategories.js';
import { selectFilter } from '../components/SelectFilter.js';
import { setLinkStyles } from './setLinkStyle.js';

export const printStoreAsideContent = async () => {
   const $aside = document.querySelector('.store-aside');
   const categories = await getCategories();

   setLinkStyles('../assets/styles/aside.css');

   $aside.innerHTML = `
      <summary>Filtros</summary>
   `;
   $aside.appendChild(selectFilter(categories));
};

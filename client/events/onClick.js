import { signOut } from '../apis/authentication.js';
import { addItemToCart } from '../apis/cart.js';
import { getCart } from '../apis/cart.js';
import { loadSignUpModal } from '../helpers/loaders/modals.js';
import { printPagination, setStyleCurrentPage } from '../helpers/store/pagination.js';
import { printProductCards } from '../helpers/store/productCards.js';

export const initCardClickEvent = ({ nodeListening, ProductData, userData, cart }) => {
   nodeListening.querySelectorAll('article').forEach((article) => {
      article.addEventListener('click', async (e) => {
         e.preventDefault();
         e.stopPropagation();

         const item = {
            product: ProductData.results.find((element) => +element.id === +article.id),
            ammount: 1,
         };

         await addItemToCart(userData, item);
         cart = await getCart(userData);
         document.querySelector('#cart').textContent = cart.results.items.length;
      });
   });
};

export const initStoreSectionclickEvent = ({ nodeListening, filters, itemsPerPage }) => {
   nodeListening.addEventListener('click', async (e) => {
      if (e.target.matches('li>span')) {
         filters['page'] = +e.target.id;
         const { productData } = await printProductCards(nodeListening, filters);
         let quantityPages = Math.ceil(productData.count / itemsPerPage);
         printPagination(nodeListening.querySelector('.pagination-container'), quantityPages, filters);
         const pages = nodeListening.querySelector('.pagination-container').querySelectorAll('span');
         setStyleCurrentPage(pages, filters['page'], 1, quantityPages);
      }
   });
};

export const initHeaderClickEvent = ({ headerNode, userData }) => {
   headerNode.addEventListener('click', async e => {
      if (e.target.matches('#sign-in')) loadSignUpModal(headerNode)
      else if (e.target.matches('#sign-out')) await signOut(userData)
      else if (e.target.matches('.burgger')) e.target.classList.toggle('active-burgger')
   })


}
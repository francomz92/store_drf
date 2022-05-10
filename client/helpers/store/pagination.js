import { Pagination } from '../../components/Pagination.js';

export const printPagination = (nodeHTML, quantityPages, filters) => {
   nodeHTML.innerHTML = '';

   if (quantityPages > 0) {
      const $pagination = Pagination({
         quantityPages: quantityPages,
         filters: filters,
      });

      $pagination.children[0].firstChild.classList.add('disabled');

      $pagination.children[1].firstChild.classList.add('active-page');

      nodeHTML.appendChild($pagination);
   }
};

export const setStyleCurrentPage = (nodeContainer, currentPage, minPage, maxPage) => {
   nodeContainer.forEach((page) => {
      if (+page.classList.contains('active-page')) {
         page.classList.remove('active-page');
      }
      if (maxPage <= 1) {
         page.classList.add('disabled');
      } else {
         if (currentPage === minPage && !Boolean(+page.textContent)) {
            page.classList.add('disabled');
            nodeContainer[nodeContainer.length - 1].classList.remove('disabled');
         }
         if (currentPage === maxPage && !Boolean(+page.textContent)) {
            page.classList.add('disabled');
            nodeContainer[0].classList.remove('disabled');
         }
         if (currentPage > minPage && currentPage < maxPage) {
            page.classList.remove('disabled');
         }
         if (+page.id === currentPage && Boolean(+page.textContent) === true) {
            page.setAttribute('class', 'active-page');
         }
      }
   });
};

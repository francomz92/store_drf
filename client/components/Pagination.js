export const pagination = ({ quantityPages, filters }) => {
   const $navPagination = document.createElement('nav');

   $navPagination.classList.add('pagination');

   $navPagination.innerHTML = `
         <li><span id="${filters.page > 1 ? filters.page - 1 : 1}">Prev</span></li>
         <li><span id="1">First</span></li>
      `;

   if (quantityPages <= 10) {
      for (let i = 1; i < quantityPages + 1; i++) {
         $navPagination.innerHTML += `<li><span id="${i}">${i}</span></li>`;
      }
   } else {
      for (let i = filters.page; i < filters.page + 3; i++) {
         if (i <= quantityPages) {
            $navPagination.innerHTML += `<li><span id="${i}">${i}</span></li>`;
         }
      }
   }

   $navPagination.innerHTML += `
      <li><span id="${quantityPages}">Last</span></li>
      <li><span id="${filters.page < quantityPages ? filters.page + 1 : quantityPages}">Next</span></li>
      `;

   return $navPagination;
};

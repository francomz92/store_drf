export const pagination = ({ quantityPages, filters }) => {
   const $navPagination = document.createElement('nav');

   $navPagination.classList.add('pagination');

   $navPagination.innerHTML = `
         <li><span id="${filters.page > 1 ? filters.page - 1 : 1}">Prev</span></li>
      `;

   $navPagination.innerHTML += `
               <li><span id="1">First</span></li>
            `;
   if (quantityPages <= 10) {
      for (let i = 1; i < quantityPages + 1; i++) {
         $navPagination.innerHTML += `
            <li><span id="${i}">${i}</span></li>
            `;
      }
      // if (filters.page > 1) {
      // }
   } else {
      for (let i = filters.page; i < filters.page + 3; i++) {
         if (i <= quantityPages) {
            $navPagination.innerHTML += `
               <li><span id="${i}">${i}</span></li>
               `;
         }
      }

      // for (let i = quantityPages - 2; i <= quantityPages; i++) {
      //    $navPagination.innerHTML += `
      //       <li><span id="${i}">${i}</span></li>
      //    `;
      // }
      // for (let i = 1; i < 4; i++) {
      //    $navPagination.innerHTML += `
      //       <li><span id="${i}">${i}</span></li>
      //       `;
      //    if (i === 3) {
      //       $navPagination.innerHTML += `
      //          <li><span>...</span></li>
      //          `;
      //    }
      //    $navPagination.innerHTML += `
      //       <li><span id="${i}">${quantityPages + 1 - i}</span></li>
      //    `;
      // }
   }

   $navPagination.innerHTML += `
      <li><span id="${quantityPages}">Last</span></li>
      `;

   $navPagination.innerHTML += `
      <li><span id="${filters.page < quantityPages ? filters.page + 1 : quantityPages}">Next</span></li>
   `;

   return $navPagination;
};

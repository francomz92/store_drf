export const filterContainer = ({ labelName = '', labelReference = '', filter }) => {
   const $divContainer = document.createElement('div');

   if (labelName !== '') {
      const $labelForFilter = document.createElement('label');
      $labelForFilter.setAttribute('for', labelReference);
      $labelForFilter.textContent = labelName;
      $divContainer.appendChild($labelForFilter);
   }

   $divContainer.classList.add('aside-filter-container');
   $divContainer.appendChild(filter);

   return $divContainer;
};

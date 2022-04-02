export const filterContainer = ({ labelName = '', labelReference = '', filter }) => {
   const $divContainer = document.createElement('div');
   const $labelForFilter = document.createElement('label');

   $divContainer.classList.add('aside-filter-container');
   $labelForFilter.setAttribute('for', labelReference);
   $labelForFilter.textContent = labelName;

   $divContainer.appendChild($labelForFilter);
   $divContainer.appendChild(filter);

   return $divContainer;
};

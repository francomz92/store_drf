export const selectFilter = ({ nameAttr, objArray, styles = [], placeHolder = '' }) => {
   const $select = document.createElement('select');

   $select.setAttribute('name', nameAttr);
   if (styles.length > 0) {
      styles.forEach((style) => $select.classList.add(style));
   }

   $select.innerHTML = `
      <option selected value="">${placeHolder}</option>
   `;

   objArray.forEach((obj) => {
      const $option = document.createElement('option');
      $option.setAttribute('value', obj.name);
      $option.textContent = obj.alias || obj.name;
      $select.appendChild($option);
   });

   return $select;
};

export const selectFilter = (nameAttr, objArray) => {
   const $select = document.createElement('select');

   $select.setAttribute('name', nameAttr);
   $select.innerHTML = `
      <option selected value="">Todos</option>
   `;

   objArray.forEach((obj) => {
      const $option = document.createElement('option');
      $option.setAttribute('value', obj.name);
      $option.textContent = obj.name;
      $select.appendChild($option);
   });

   return $select;
};

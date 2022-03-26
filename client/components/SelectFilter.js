export const selectFilter = (categories) => {
   const $select = document.createElement('select');

   $select.setAttribute('name', 'category');
   $select.innerHTML = `
      <option selected value="">Elige una categoría</option>
   `;

   categories.forEach((category) => {
      const $option = document.createElement('option');
      $option.setAttribute('value', category.name);
      $option.textContent = category.name;
      $select.appendChild($option);
   });

   return $select;
};

export const searchFilter = ({ nameAttr, placeHolder = '', listId = '', styles = [] }) => {
   const $searchInput = document.createElement('input');

   $searchInput.setAttribute('type', 'search');
   $searchInput.setAttribute('name', nameAttr);
   $searchInput.setAttribute('placeholder', placeHolder);
   $searchInput.setAttribute('autocomplete', 'off');

   if (listId.length > 0) {
      $searchInput.setAttribute('list', listId);
   }

   if (styles.length > 0) {
      styles.forEach((style) => $searchInput.classList.add(style));
   }

   return $searchInput;
};

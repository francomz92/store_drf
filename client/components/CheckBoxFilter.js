export const checkBoxFilter = (nameAttr) => {
   const $check = document.createElement('input');
   $check.setAttribute('type', 'checkbox');
   $check.setAttribute('name', nameAttr);
   return $check;
};

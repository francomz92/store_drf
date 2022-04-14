export const rangeFilter = (firstNameAttr, secondNameAttr) => {
   const $container = document.createElement('div');
   const $desdeInput = document.createElement('input');
   const $desdeSpan = document.createElement('span');
   const $hastaSpan = document.createElement('span');
   const $hastaInput = document.createElement('input');

   $desdeSpan.textContent = 'Desde:';
   $hastaSpan.textContent = 'Hasta:';

   $desdeInput.setAttribute('type', 'range');
   $desdeInput.setAttribute('min', '0');
   $desdeInput.setAttribute('max', '45000');
   $desdeInput.setAttribute('value', '0');
   $desdeInput.setAttribute('step', '5000');
   $desdeInput.setAttribute('name', firstNameAttr);

   $hastaInput.setAttribute('type', 'range');
   $hastaInput.setAttribute('min', '5000');
   $hastaInput.setAttribute('max', '50000');
   $hastaInput.setAttribute('value', '50000');
   $hastaInput.setAttribute('step', '5000');
   $hastaInput.setAttribute('name', secondNameAttr);

   $container.append($desdeSpan, $desdeInput, $hastaSpan, $hastaInput);

   return $container;
};

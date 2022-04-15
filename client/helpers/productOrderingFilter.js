import { selectFilter } from '../components/SelectFilter.js';

export const printProductOrderingSelect = (nodeHTML) => {
   nodeHTML.appendChild(
      selectFilter({
         nameAttr: 'ordering',
         objArray: [
            { name: 'unit_price', alias: 'Menor Precio' },
            { name: '-unit_price', alias: 'Mayor Precio' },
         ],
         styles: ['ordering-select'],
         placeHolder: 'Ordenar',
      })
   );
};

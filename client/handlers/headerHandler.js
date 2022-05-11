import { printHeader } from '../helpers/header.js';
import { initHeaderClickEvent} from '../events/onClick.js'

export const headerHandler = (userData, cart) => {
   const $header = printHeader(userData, cart);

   initHeaderClickEvent({headerNode: $header, userData: userData})

   return $header;
};

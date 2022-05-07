import { printHeader } from '../helpers/header.js';

export const headerHandler = (userData, cart) => {
   const $header = printHeader(userData, cart);
   return $header;
};

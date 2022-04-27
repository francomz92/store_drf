import { header } from '../components/Header.js';
import { loadStyles } from './linkStyle.js';

export const printHeader = (userData, cart) => {
   loadStyles('../assets/styles/index.header.css');
   const $header = header(userData, cart);
   document.body.insertAdjacentElement('afterbegin', $header);
   return $header;
};

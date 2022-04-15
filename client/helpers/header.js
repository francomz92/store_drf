import { header } from '../components/Header.js';
import { loadStyles } from './linkStyle.js';

export const printHeader = (userData, cart) => {
   loadStyles('../assets/styles/index.header.css');
   document.body.insertAdjacentElement('afterbegin', header(userData, cart));
};

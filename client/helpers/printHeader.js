import { header } from '../components/Header.js';
import { setLinkStyles } from './setLinkStyle.js';

export const printHeader = (userData, cart) => {
   setLinkStyles('../assets/styles/index.header.css');
   document.body.insertAdjacentElement('afterbegin', header(userData, cart));
};

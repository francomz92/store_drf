import { header } from '../components/Header.js';
import { setLinkStyles } from './setLinkStyle.js';

export const printHeader = (userData) => {
   setLinkStyles('../assets/styles/index.header.css');
   document.body.insertAdjacentElement('afterbegin', header(userData));
};

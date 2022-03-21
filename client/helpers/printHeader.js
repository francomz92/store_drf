import { header } from '../components/Header.js';
import { setLinkStyles } from './setLinkStyle.js';

export const printHeader = (user) => {
   setLinkStyles('../assets/styles/index.header.css');
   document.body.insertAdjacentElement('afterbegin', header(user));
};

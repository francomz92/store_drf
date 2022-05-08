import { header } from '../components/Header.js';
import { loadStyles } from './linkStyle.js';

export const printHeader = (userData, cart) => {
   loadStyles('../assets/styles/index.header.css');
   const $header = header(userData, cart);
   document.body.insertAdjacentElement('afterbegin', $header);
   return $header;
};

export const setStyleActiveLink = (nodeContainer, HTMLTag) => {
   const $links = nodeContainer.querySelectorAll(HTMLTag);

   $links.forEach((link) => {
      if (link.href.includes(`/${location.hash}`)) {
         link.classList.add('active-link');
      } else link.classList.remove(['active-link']);
   });
};

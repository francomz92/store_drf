import { Header } from '../components/Header.js';
import { loadStyles } from './linkStyle.js';

export const printHeader = (userData, cart) => {
   loadStyles('../assets/styles/index.header.css');
   const $header = Header(userData, cart);
   document.body.insertAdjacentElement('afterbegin', $header);
   return $header;
};

export const setStyleActiveLink = (nodeContainer, HTMLTag) => {
   const $links = nodeContainer.querySelectorAll(HTMLTag);

   $links.forEach((link) => {
      if (location.hash !== '' && link.href.includes(`/${location.hash}`)) {
         link.classList.add('active-link');
      } else if (location.hash !== '' && !link.href.includes(`/${location.hash}`)) {
         link.classList.remove(['active-link']);
      } else if (link.href.includes('/#home')) {
         link.classList.add('active-link');
      }
   });
};

import { printHeader } from './helpers/header.js';
import { storeSectionHandler } from './handlers/storeSectionHandler.js';
import { getCart } from './apis/getCart.js';
import { loadStyles } from './helpers/linkStyle.js';

const user = localStorage.getItem('user');
let userData = null;
let cart = null;

document.addEventListener('DOMContentLoaded', async (e) => {
   const $main = document.getElementById('sections');
   if (user) {
      userData = JSON.parse(user);
      cart = await getCart(userData);
   }
   printHeader(userData, cart);

   if (location.hash === '#store') {
      document.head.querySelector('title').textContent = 'Store';
      loadStoreSection($main);
   } else if (location.hash === '#contact') {
      document.head.querySelector('title').textContent = 'Contact';
   } else document.head.querySelector('title').textContent = 'Home';

   window.addEventListener('hashchange', (e) => {
      if (e.newURL.match('/#store')) {
         // loadStyles('../assets/styles/section.store.css');
         // loadStyles('../assets/styles/aside.css');
         // loadStyles('./assets/styles/card.css');
         // storeSectionHandler($main, userData, cart);
         document.head.querySelector('title').textContent = 'Store';
         loadStoreSection($main);
      } else if (e.newURL.match('/#contact')) {
         document.head.querySelector('title').textContent = 'Contact';
         $main.innerHTML = '';
      } else {
         document.head.querySelector('title').textContent = 'Home';
         $main.innerHTML = '';
      }
   });
});

function loadSection({ nodeMain, data = [], callback, stylesDir = [] }) {
   if (stylesDir.length > 0) {
      stylesDir.forEach((style) => loadStyles(style));
   }
   callback(nodeMain, ...data);
}

function loadStoreSection(main) {
   loadSection({
      nodeMain: main,
      data: [userData, cart],
      callback: storeSectionHandler,
      stylesDir: [
         '../assets/styles/section.store.css',
         '../assets/styles/aside.css',
         './assets/styles/card.css',
      ],
   });
}

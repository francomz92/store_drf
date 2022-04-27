import { getCart } from './apis/cart.js';
import { loadStoreSection } from './helpers/loaders/storeSection.js';
import { headerHandler } from './handlers/headerHandler.js';

const user = localStorage.getItem('user');
let userData = null;
let cart = null;

document.addEventListener('DOMContentLoaded', async (e) => {
   const $main = document.getElementById('sections');
   if (user) {
      userData = JSON.parse(user);
      cart = await getCart(userData);
   }

   headerHandler(userData, cart);

   // On load specific path url
   if (location.hash === '#store') {
      document.head.querySelector('title').textContent = 'Store';
      loadStoreSection($main, userData, cart);
   } else if (location.hash === '#contact') {
      document.head.querySelector('title').textContent = 'Contact';
   } else document.head.querySelector('title').textContent = 'Home';

   // On change path url event
   window.addEventListener('hashchange', (e) => {
      if (e.newURL.match('/#store')) {
         document.head.querySelector('title').textContent = 'Store';
         loadStoreSection($main, userData, cart);
      } else if (e.newURL.match('/#contact')) {
         document.head.querySelector('title').textContent = 'Contact';
         $main.innerHTML = '';
      } else {
         document.head.querySelector('title').textContent = 'Home';
         $main.innerHTML = '';
      }
   });
});

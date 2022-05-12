import { getCart } from './apis/cart.js';
import { loadStoreSection } from './helpers/loaders/storeSection.js';
import { headerHandler } from './handlers/headerHandler.js';
import { setStyleActiveLink } from './helpers/header.js';

const user = localStorage.getItem('user');
let userData = null;
let cart = null;

document.addEventListener('DOMContentLoaded', async (e) => {
   const $main = document.getElementById('sections');
   if (user) {
      userData = JSON.parse(user);
      cart = await getCart(userData);
   }

   const $header = headerHandler(userData, cart);

   // On load specific path url
   setStyleActiveLink($header.querySelector('nav'), 'a');

   switch (location.hash) {
      case '#store':
         document.head.querySelector('title').textContent = 'Store';
         loadStoreSection($main, userData, cart);
         break;
      case '#contact':
         document.head.querySelector('title').textContent = 'Contact';
         break;
      default:
         document.head.querySelector('title').textContent = 'Home';
         break;
   }

   // On change path url event
   window.addEventListener('hashchange', (e) => {
      setStyleActiveLink($header.querySelector('nav'), 'a');

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

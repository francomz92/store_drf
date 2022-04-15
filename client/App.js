import { printHeader } from './helpers/header.js';
import { storeSectionHandler } from './handlers/storeSectionHandler.js';
import { getCart } from './apis/getCart.js';

const user = localStorage.getItem('user');
let userData = null;
let cart = null;

document.addEventListener('DOMContentLoaded', async (e) => {
   if (user) {
      userData = JSON.parse(user);
      cart = await getCart(userData);
   }
   printHeader(userData, cart);
   storeSectionHandler(userData, cart);
});

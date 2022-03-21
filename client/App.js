import { prinProductCards } from './helpers/printProductCards.js';
import { printHeader } from './helpers/printHeader.js';
import { printStoreAsideContent } from './helpers/printStoreAsideContent.js';

const user = localStorage.getItem('user');

document.addEventListener('DOMContentLoaded', (e) => {
   let userData = null;
   if (user) userData = JSON.parse(user).user;
   printHeader(userData);
   prinProductCards();
   printStoreAsideContent();
});

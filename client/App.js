import { printHeader } from './helpers/printHeader.js';
import { printStoreSection } from './helpers/printStoreSection.js';

const user = localStorage.getItem('user');

document.addEventListener('DOMContentLoaded', (e) => {
   let userData = null;
   if (user) userData = JSON.parse(user).user;
   printHeader(userData);
   printStoreSection();
});

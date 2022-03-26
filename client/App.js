import { printHeader } from './helpers/printHeader.js';
import { storeSectionHandler } from './handlers/storeSectionHandler.js';

const user = localStorage.getItem('user');

document.addEventListener('DOMContentLoaded', async (e) => {
   let userData = null;
   if (user) userData = JSON.parse(user);
   printHeader(userData.user);
   storeSectionHandler(userData);
});

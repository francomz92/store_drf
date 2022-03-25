import { setLinkStyles } from './setLinkStyle.js';
import { printStoreAsideContent } from './printStoreAsideContent.js';
import { prinProductCards } from './printProductCards.js';

export const printStoreSection = () => {
   setLinkStyles('../assets/styles/section.store.css');
   prinProductCards();
   printStoreAsideContent();
};

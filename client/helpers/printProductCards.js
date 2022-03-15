import { card } from '../components/Card.js';
import { getProductsData } from '../apis/getProducts.js';

const setLinkStyles = () => {
   const $link = document.createElement('link');
   $link.setAttribute('href', './assets/styles/card.css');
   $link.setAttribute('rel', 'stylesheet');
   document.head.appendChild($link);
};

export const prinProductCards = async () => {
   const $grid = document.getElementById('card-grid');
   const data = await getProductsData();
   if (data.results.length > 0) {
      setLinkStyles();
      data.results.forEach((product) => {
         $grid.appendChild(card(product));
      });
   }
};

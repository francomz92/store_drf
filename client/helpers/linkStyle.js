export const loadStyles = (directory) => {
   const $link = document.createElement('link');
   $link.setAttribute('href', directory);
   $link.setAttribute('rel', 'stylesheet');
   document.head.appendChild($link);
};

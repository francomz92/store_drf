import { loadStyles } from './linkStyle.js';

export const loadSection = ({ nodeMain, data = [], callback, stylesDir = [] }) => {
   if (stylesDir.length > 0) {
      stylesDir.forEach((style) => loadStyles(style));
   }
   callback(nodeMain, ...data);
};

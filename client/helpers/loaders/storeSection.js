import { loadSection } from '../sectionLoader.js';
import { storeSectionHandler } from '../../handlers/storeSectionHandler.js';

export const loadStoreSection = (main, userData, cart) => {
   loadSection({
      nodeMain: main,
      data: [userData, cart],
      callback: storeSectionHandler,
      stylesDir: [
         '../../assets/styles/section.store.css',
         '../../assets/styles/aside.css',
         '../../assets/styles/card.css',
      ],
   });
};

/* 
   queryFilters valid
   {
      category__name: 'String',
      name: 'String',
      unit_price: Number,
      offer: 'Boolean',
   };
*/

const getFilters = (filters) => {
   let setedFilters = '';
   for (const key in filters) {
      if (Object.hasOwnProperty.call(filters, key) && Boolean(filters[key]) !== false) {
         setedFilters += `${key}=${filters[key]}&`;
      }
   }
   if (setedFilters.endsWith('&')) {
      setedFilters = setedFilters.slice(0, setedFilters.length - 1);
   }
   return setedFilters;
};

export const getProductsData = async (queryFilters) => {
   try {
      const filters = getFilters(queryFilters);
      const response = await fetch(`http://localhost:8000/api/shop/products/public/?${filters}`);
      const products = await response.json();
      if (!response.ok) throw response;
      return products;
   } catch (error) {
      console.log(error.statusText || 'Error');
   }
};

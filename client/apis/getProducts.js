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
      if (Object.hasOwnProperty.call(filters, key) && filters[key] !== null) {
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
      const response = await fetch(`http://localhost:8000/api/shop/public/products/?${filters}`);
      const productsData = await response.json();
      if (!response.ok) throw response;
      return productsData;
   } catch (error) {
      alert(error.statusText || 'Error');
   }
};

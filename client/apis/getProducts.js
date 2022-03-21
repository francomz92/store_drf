export const getProductsData = async () => {
   try {
      const response = await fetch('http://localhost:8000/api/shop/products/public/');
      const products = await response.json();
      if (!response.ok) throw response;
      return products;
   } catch (error) {
      console.log(error.statusText || 'Error');
   }
};

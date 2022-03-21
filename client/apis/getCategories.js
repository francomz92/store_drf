export const getCategories = async () => {
   try {
      const response = await fetch('http://localhost:8000/api/shop/public/category/');
      const categoriesData = await response.json();
      if (!response.ok) throw response;
      return categoriesData.results;
   } catch (error) {
      console.log(error.statusText || 'Error');
   }
};

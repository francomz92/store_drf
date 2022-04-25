export const addItemToCart = async (userData, item) => {
   try {
      const response = await fetch(
         `http://localhost:8000/api/shop/private/cart/${userData.user.id}/cart_items/`,
         {
            method: 'POST',
            body: JSON.stringify(item),
            headers: {
               'content-Type': 'application/json',
               Authorization: `test ${userData.accessToken}`,
            },
         }
      );
      if (!response.ok) throw response;
   } catch (error) {
      alert(error.statusText || 'Error');
   }
};

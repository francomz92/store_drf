export const getCart = async (userData) => {
   try {
      const cartResponse = await fetch(
         `http://localhost:8000/api/shop/cart/${userData.user.id}/cart_items/`,
         {
            headers: {
               'content-Type': 'application/json',
               Authorization: `test ${userData.accessToken}`,
            },
         }
      );
      const cartData = await cartResponse.json();
      if (!cartResponse.ok) throw cartResponse;
      return cartData;
   } catch (error) {
      alert(error.statusText || 'Error');
   }
};

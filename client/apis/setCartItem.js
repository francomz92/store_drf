export const setCartItem = async (userData, item) => {
   try {
      const response = await fetch(`http://localhost:8000/api/shop/cart/${userData.user.id}/cart_items/`, {
         method: 'POST',
         body: JSON.stringify(item),
         headers: {
            'content-Type': 'application/json',
            Authorization: `test ${userData.accessToken}`,
         },
      });
      if (!response.ok) throw response;
   } catch (error) {
      console.log(error.statusText || 'Error');
   }
};

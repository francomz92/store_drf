export const getCart = async (userData) => {
   try {
      const response = await fetch(`http://localhost:8000/api/shop/cart/${userData.user.id}/cart_items/`, {
         headers: {
            'content-Type': 'application/json',
            Authorization: `test ${userData.accessToken}`,
         },
      });
      const cartData = await response.json();
      if (!response.ok) throw response;
      return cartData;
   } catch (error) {
      alert(error.statusText || 'Error');
   }
};

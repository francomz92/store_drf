import { expiredToken } from "../helpers/errors.js";

export const getCart = async (userData) => {
   try {
      const response = await fetch(
         `http://localhost:8000/api/shop/private/cart/${userData.user.id}/cart_items/`,
         {
            headers: {
               'content-Type': 'application/json',
               Authorization: `test ${userData.access}`,
            },
         }
      );
      const cartData = await response.json();
      if (!response.ok) throw response;
      return cartData;
   } catch (error) {
      if (error.status === 401) {
         expiredToken()
      }
   }
};

export const addItemToCart = async (userData, item) => {
   try {
      const response = await fetch(
         `http://localhost:8000/api/shop/private/cart/${userData.user.id}/cart_items/`,
         {
            method: 'POST',
            body: JSON.stringify(item),
            headers: {
               'content-Type': 'application/json',
               Authorization: `test ${userData.access}`,
            },
         }
      );
      if (!response.ok) throw response;
      return true
   } catch (error) {
      if (error.status === 401) {
         expiredToken()
      }
   }
};

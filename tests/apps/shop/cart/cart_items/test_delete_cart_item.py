from .dependencies_imports import *


class TestPublicDeleteCartItemView(APITestCase):

   def setUp(self):
      self.user = get_or_create_user(email='test@email.com', dni='12345678', password='testpassword')
      category = create_category(name='Test Category')
      self.product = create_product(category=category,
                                    description='description1',
                                    unit_price=10.0,
                                    stok=10,
                                    image_url=None,
                                    offer=True,
                                    discount_rate=10)
      self.cart_item = create_cart_item(cart=self.user.user_cart, product=self.product, ammount=2)
      self.client = APIClient()
      return super().setUp()

   def test_try_to_delete_cart_item_without_auth(self):
      """
         Test that a user can't delete a cart item without being authenticated.
         This operation should return a 401 status code.
      """
      print('Test 1')
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=self.user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.delete(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateDeleteCartItemView(APITestCase):

   def setUp(self):
      self.user = get_or_create_user(email='test@email.com', dni='12345678', password='testpassword')
      category = create_category(name='Test Category')
      self.product = create_product(category=category,
                                    description='description1',
                                    unit_price=10.0,
                                    stok=10,
                                    image_url=None,
                                    offer=True,
                                    discount_rate=10)
      self.cart_item = create_cart_item(cart=self.user.user_cart, product=self.product, ammount=2)
      self.client = APIClient()
      self.client.force_authenticate(user=self.user)
      return super().setUp()

   def test_delete_cart_item_with_valid_data(self):
      """
         Test that a user can delete a cart item with valid data.
         This operation should return a 204 status code.
      """
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=self.user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.delete(url, format='json')
      item = cart_models.CartItem.objects.filter(id=getattr(self.cart_item, 'id')).first()
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertIsNone(item)

   def test_try_to_delete_cart_item_in_another_user(self):
      """
         Test that a user can't delete a cart item in another user.
         This operation should return a 403 status code.
      """
      user = get_or_create_user(email='another_user@email.com', dni='11122221', password='testpassword')
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.delete(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
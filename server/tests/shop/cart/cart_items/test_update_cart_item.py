from .dependencies_imports import *


class TestPublicUpdateCartItemView(APITestCase):

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

   def test_try_to_update_cart_item_without_auth(self):
      """
         Test that a user can't update a cart item without being authenticated.
         This operation should return a 401 status code.
      """
      payload = {'ammount': self.cart_item.ammount + 1}
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=self.user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.put(url, data=payload, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateUpdateCartItemView(APITestCase):

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

   def test_update_cart_item_with_valid_data(self):
      """
         Test that a user can update a cart item with valid data.
         This operation should return a 200 status code and the updated cart item.
      """
      payload = {'ammount': self.cart_item.ammount + 1}
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=self.user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.put(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(id=getattr(self.cart_item, 'id')).first()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIsNotNone(item)
      self.assertEqual(getattr(item, 'ammount'), payload['ammount'])

   def test_try_to_update_with_ammount_lt_one(self):
      """
         Test that a user can update a cart item with ammount lt 1.
         This operation should return a 200 status code and delete item.
      """
      payload = {'ammount': -1}
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=self.user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.put(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(id=getattr(self.cart_item, 'id')).first()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIsNone(item)

   def test_try_to_update_cart_item_with_ammount_greater_than_stok(self):
      """
         Test that a user can't update a cart item with ammount greater than stok.
         This operation should return a 400 status code.
      """
      payload = {'ammount': self.product.stok + 1}
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=self.user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.put(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(id=getattr(self.cart_item, 'id')).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertEqual(getattr(item, 'ammount'), self.cart_item.ammount)

   def test_try_to_update_cart_item_in_another_user(self):
      """
         Test that a user can't update a cart item in another user.
         This operation should return a 403 status code.
      """
      payload = {'ammount': 1}
      user = get_or_create_user(email='another_user@email.com', dni='11122221', password='testpassword')
      url = get_cart_item_url(name='private_cart_item_detail',
                              user_id=user.id,
                              item_id=getattr(self.cart_item, 'id'))
      response = self.client.put(url, data=payload, format='json')
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
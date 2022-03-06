from .dependencies_imports import *


class TestPublicCreateCartItemView(APITestCase):

   def setUp(self):
      self.user = get_or_create_user(email='test@email.com', dni='12345678', password='testpassword')
      category = create_category(name='Test Category')
      self.products = [
          create_product(category=category,
                         description='description1',
                         unit_price=1.0,
                         stok=10,
                         image_url=None,
                         offer=True,
                         discount_rate=10) for i in range(3)
      ]
      self.client = APIClient()
      return super().setUp()

   def test_try_to_create_cart_item_without_auth(self):
      """
         Test that a user can't create a cart item without being authenticated.
      """
      payload = {
          'product': product_serializers.ProductSerializer(self.products[0]).data,
          'ammount': 2,
      }
      url = get_cart_item_url(name='private_cart_items', user_id=self.user.id)
      response = self.client.post(url, data=payload, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateCreateCartItemView(APITestCase):

   def setUp(self):
      self.user = get_or_create_user(email='test@email.com', dni='12345678', password='testpassword')
      category = create_category(name='Test Category')
      self.products = [
          create_product(category=category,
                         description='description1',
                         unit_price=1.0,
                         stok=10,
                         image_url=None,
                         offer=True,
                         discount_rate=10) for i in range(3)
      ]
      self.client = APIClient()
      self.client.force_authenticate(user=self.user)
      return super().setUp()

   def test_create_cart_item_with_auth(self):
      """
         Test that a user can create a cart item with being authenticated.
         This operation should return a 201 status code and create a cart item.
      """
      payload = {
          'product': product_serializers.ProductSerializer(self.products[0]).data,
          'ammount': 2,
      }
      url = get_cart_item_url(name='private_cart_items', user_id=self.user.id)
      response = self.client.post(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(cart__user=self.user, product=self.products[0]).first()
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertIsNotNone(item)
      self.assertEqual(getattr(item, 'product'), self.products[0])
      self.assertEqual(getattr(item, 'ammount'), payload['ammount'])

   def test_try_to_create_cart_item_with_invalid_data(self):
      """
         Test that a user can't create a cart item with invalid data.
         This operation should return a 400 status code and not create a cart item.
      """
      payload = {
          'product': {
              **product_serializers.ProductSerializer(self.products[0]).data,
          },
          'ammount': 'invalid',
      }
      url = get_cart_item_url(name='private_cart_items', user_id=self.user.id)
      response = self.client.post(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(cart__user=self.user, product=self.products[0]).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(item)

   def test_try_to_create_cart_item_in_another_user(self):
      """
         Test that a user can't create a cart item in another user's cart.
         This operation should return a 403 status code and not create a cart item.
      """
      other_user = get_or_create_user(email='another_user@email.com', dni='11111111', password='testpassword')
      payload = {
          'product': {
              **product_serializers.ProductSerializer(self.products[1]).data,
          },
          'ammount': 3,
      }
      url = get_cart_item_url(name='private_cart_items', user_id=other_user.id)
      response = self.client.post(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(cart__user=other_user, product=self.products[1]).first()
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
      self.assertIsNone(item)

   def test_try_to_create_cart_item_without_stok(self):
      """
         Test that a user can't create a cart item with a product that has no stok.
         This operation should return a 400 status code and not create a cart item.
      """
      product = create_product(category=self.products[0].category,
                               description='asdasda',
                               unit_price=1.0,
                               offer=True,
                               discount_rate=10,
                               stok=0)
      payload = {
          'product': {
              **product_serializers.ProductSerializer(product).data,
          },
          'ammount': 3,
      }
      url = get_cart_item_url(name='private_cart_items', user_id=self.user.id)
      response = self.client.post(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(cart__user=self.user, product=product).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(item)
   
   def test_try_to_create_cart_item_with_product_stok_insufficient(self):
      """
         Test that a user can't create a cart item with a product that has insufficient stok.
         This operation should return a 400 status code and not create a cart item.
      """
      product = create_product(category=self.products[0].category,
                               description='asdasda',
                               unit_price=1.0,
                               offer=True,
                               discount_rate=10,
                               stok=1)
      payload = {
          'product': {
              **product_serializers.ProductSerializer(product).data,
          },
          'ammount': 3,
      }
      url = get_cart_item_url(name='private_cart_items', user_id=self.user.id)
      response = self.client.post(url, data=payload, format='json')
      item = cart_models.CartItem.objects.filter(cart__user=self.user, product=product).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(item)
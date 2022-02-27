from .dependencies_imports import *

product_payload: Dict[str, Any] = {
    'name': 'some_product',
    'description': 'description 1',
    'unit_price': 1.0,
    'stok': 10,
    'image_url': None,
    'offer': True,
    'discount_rate': 10,
}


class TestPublicCartItemsListView(APITestCase):

   def setUp(self):
      user = get_or_create_user(email='test@email.com', dni='12345678', password='testpassword')
      category = create_category(name='Test Category')
      product = create_product(category=category, **product_payload)
      self.cart = cart_models.Cart.objects.get(user=user)
      create_cart_item(cart=self.cart, product=product, ammount=1)
      self.url = get_cart_item_url('private_cart_items', user_id=user.id)
      self.client = APIClient()
      return super().setUp()

   def test_try_to_get_list_of_cart_items_without_authentication(self):
      """
         Try to get a list of cart items without authentication.
         This operation should return a status code 401.
      """
      response = self.client.get(self.url, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateCartItemsListView(APITestCase):

   def setUp(self):
      user = get_or_create_user(email='test@email.com', dni='12345678', password='testpassword')
      category = create_category(name='Test Category')
      product = create_product(category=category, **product_payload)
      self.cart = cart_models.Cart.objects.get(user=user)
      create_cart_item(cart=self.cart, product=product, ammount=1)
      self.url = get_cart_item_url('private_cart_items', user_id=user.id)
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_get_list_of_cart_items(self):
      """
         Get a list of cart items.
         This operation should return a status code 200 and a list of cart items.
      """
      cart_items = cart_models.CartItem.objects.filter(cart=self.cart)
      response = self.client.get(self.url, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(data['results']), cart_items.count())
      self.assertEqual(data['results'], serializers.CartItemSerializer(cart_items, many=True).data)

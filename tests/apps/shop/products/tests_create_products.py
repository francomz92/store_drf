from .dependencies_imports import *

PRIVATE_PRODUCTS_URL = reverse_lazy('shop:products:private_products')


class TestPriveteCreateProductsView(APITestCase):

   product_payload: Dict[str, Any] = {
       'name': 'some_product',
       'description': 'description 1',
       'unit_price': 1.0,
       'stok': 10,
       'image_url': '',
       'offer': True,
       'discount_rate': 10,
   }

   def setUp(self) -> None:
      self.product = self.product_payload
      category = category_models.Category.objects.get_or_create(name='some_category')[0]
      self.product.setdefault('category', category_serializers.CategorySerializer(category).data['name'])
      user = get_or_create_user(email='root', dni='12345678', password='root')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_create_product_with_valid_payload(self):
      """
         Create a product with valid payload.
         This operation should return a status code 201 and the product created.
      """
      response = self.client.post(PRIVATE_PRODUCTS_URL, self.product, format='json')
      data = response.json()
      product = models.Product.objects.filter(id=data['id']).first()
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertIsNotNone(product)
      self.assertEqual(data, serializers.ProductSerializer(product).data)

   def test_try_to_create_product_with_invalid_data(self):
      """
         Try to create a product with invalid data.
         This operation should return a status code 400.
      """
      new_product = self.product.copy()
      new_product.update({'unit_price': 'invalid_unit_price'})
      response = self.client.post(PRIVATE_PRODUCTS_URL, new_product, format='json')
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

   def test_try_to_create_product_without_some_required_data(self):
      """
         Try to create a product without some required data.
         This operation should return a status code 400.
      """
      new_product = {**self.product}
      new_product.update({'name': None})
      response = self.client.post(PRIVATE_PRODUCTS_URL, new_product, format='json')
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestPublicCreateProductsView(APITestCase):

   product_payload: Dict[str, Any] = {
       'name': 'some_product',
       'description': 'description 1',
       'unit_price': 1.0,
       'stok': 10,
       'image_url': '',
       'offer': True,
       'discount_rate': 10,
   }

   def setUp(self) -> None:
      self.product = self.product_payload
      category = category_models.Category.objects.get_or_create(name='some_category')[0]
      self.product.setdefault('category', category_serializers.CategorySerializer(category).data['name'])
      self.client = APIClient()
      return super().setUp()

   def test_create_product_with_valid_payload(self):
      """
         Create a product with valid payload.
         This operation should return a status code 401.
      """
      response = self.client.post(PRIVATE_PRODUCTS_URL, self.product, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

   def test_try_to_create_product_with_invalid_data(self):
      """
         Try to create a product with invalid data.
         This operation should return a status code 401.
      """
      new_product = self.product.copy()
      new_product.update({'unit_price': 'invalid_unit_price'})
      response = self.client.post(PRIVATE_PRODUCTS_URL, new_product, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

   def test_try_to_create_product_without_some_required_data(self):
      """
         Try to create a product without some required data.
         This operation should return a status code 401.
      """
      new_product = {**self.product}
      new_product.update({'name': None})
      response = self.client.post(PRIVATE_PRODUCTS_URL, new_product, format='json')
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

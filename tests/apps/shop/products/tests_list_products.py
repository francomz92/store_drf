from .dependencies_imports import *


class TestPublicListProductsView(APITestCase):

   QUANTITY_OF_PRODUCTS_TO_CREATE = 3

   product_payload: Dict[str, Any] = {
       'description': 'description 1',
       'unit_price': 1.0,
       'stok': 10,
       'image_url': 'http://image_url.com',
       'offer': True,
       'discount_rate': 10,
   }

   def setUp(self) -> None:
      self.client = APIClient()
      category = create_category('some_category')
      self.payload = self.product_payload
      self.payload.setdefault('category', category)
      create_product(**self.payload, active=False)
      return super().setUp()

   def test_get_list_of_products(self):
      """
         Get a list of products.
         This operation should return a status code 200 and a list of products.
      """
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload)
      response = self.client.get(PUBLIC_PRODUCTS_URL)
      data = response.json()
      products = get_products(active=True)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(data['results']), self.QUANTITY_OF_PRODUCTS_TO_CREATE)
      self.assertEqual(data['results'], serializers.ProductSerializer(products, many=True).data)

   def test_get_list_of_products_by_valid_query_param(self):
      """
         Get a list of products by valid query param.
         This operation should return a status code 200 and a list of products that match the query param.
      """
      name = 'Product'
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload, name=f'{name}_{i}')
      response = self.client.get(PUBLIC_PRODUCTS_URL + f'?name={name}_1')
      data = response.json()
      products = get_products(active=True, name=f'{name}_1')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], serializers.ProductSerializer(products, many=True).data)

   def test_try_to_get_list_of_products_by_valid_query_param_with_value_no_registered(self):
      """
         Try to get a list of products by valid query param with value no registered.
         This operation should return a status code 200 and a empty list.
      """
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload)
      response = self.client.get(PUBLIC_PRODUCTS_URL + f'?name=Product_no_registered')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])

   def test_try_to_get_list_of_products_by_invalid_query_param(self):
      """
         Try to get a list of products by invalid query param.
         This operation should return a status code 200 and a list of products that match the query param.
      """
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload, name=f'Product_{i}')
      response = self.client.get(PUBLIC_PRODUCTS_URL + f'?invalid_param=Product_1')
      data = response.json()
      products = get_products(active=True)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(data['results']), self.QUANTITY_OF_PRODUCTS_TO_CREATE)
      self.assertEqual(data['results'], serializers.ProductSerializer(products, many=True).data)


class TestPrivateListProductsView(APITestCase):

   QUANTITY_OF_PRODUCTS_TO_CREATE = 3

   product_payload: Dict[str, Any] = {
       'description': 'description 1',
       'unit_price': 1.0,
       'stok': 10,
       'image_url': 'http://image_url.com',
       'offer': True,
       'discount_rate': 10,
   }

   def setUp(self) -> None:
      category = create_category(name='some_category')
      self.payload = self.product_payload
      self.payload.setdefault('category', category)
      create_product(**self.payload, active=False)
      self.user = get_or_create_user(email='root', dni='12345678', password='root')
      self.client = APIClient()
      self.client.force_authenticate(user=self.user)
      return super().setUp()

   def test_get_list_of_products(self):
      """
         Get a list of products.
         This operation should return a status code 200 and a list of products.
      """
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload)
      response = self.client.get(PRIVATE_PRODUCTS_URL)
      data = response.json()
      products = get_products()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(data['results']), models.Product.objects.count())
      self.assertEqual(data['results'], serializers.ProductSerializer(products, many=True).data)

   def test_get_list_of_products_by_valid_query_param(self):
      """
         Get a list of products by valid query param.
         This operation should return a status code 200 and a list of products that match the query param.
      """
      name = 'Product'
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload, name=f'{name}_{i}')
      response = self.client.get(PRIVATE_PRODUCTS_URL + f'?name={name}_1')
      data = response.json()
      products = get_products(name=f'{name}_1')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], serializers.ProductSerializer(products, many=True).data)

   def test_try_to_get_list_of_products_by_valid_query_param_with_value_no_registered(self):
      """
         Try to get a list of products by valid query param with value no registered.
         This operation should return a status code 200 and a empty list.
      """
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload)
      response = self.client.get(PRIVATE_PRODUCTS_URL + f'?name=Product_no_registered')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])

   def test_try_to_get_list_of_products_by_invalid_query_param(self):
      """
         Try to get a list of products by invalid query param.
         This operation should return a status code 200 and a list of products that match the query param.
      """
      for i in range(self.QUANTITY_OF_PRODUCTS_TO_CREATE):
         create_product(**self.payload, name=f'Product_{i}')
      response = self.client.get(PRIVATE_PRODUCTS_URL + f'?invalid_param=Product_1')
      data = response.json()
      products = get_products()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(data['results']), models.Product.objects.count())
      self.assertEqual(data['results'], serializers.ProductSerializer(products, many=True).data)
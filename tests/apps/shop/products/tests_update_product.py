from utils.tests.users import create_an_user
from .dependencies_imports import *

product_payload: Dict[str, Any] = {
    'name': 'Some product',
    'description': 'description 1',
    'unit_price': 1.0,
    'stok': 10,
    'image_url': '',
    'offer': True,
    'discount_rate': 10,
}


class TestPublicUpdateProductView(APITestCase):

   product = {**product_payload}

   def setUp(self):
      self.product.setdefault('category', create_category(name='some_category'))
      self.client = APIClient()
      return super().setUp()

   def test_try_to_update_product_without_authentication(self):
      """
         Try to update a product without authentication.
         This operation should return a status code 401.
      """
      product = create_product(**self.product)
      url = get_product_detail_url(name='private_product_detail', id=getattr(product, 'id'))
      response = self.client.put(url)
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateUpdateProductView(APITestCase):

   product = {**product_payload}

   def setUp(self):
      category = category_models.Category.objects.get_or_create(name='some_category')[0]
      self.product.setdefault('category', category)
      user = get_or_create_user(email='root', dni='12345678', password='root')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_update_product_with_valid_data(self):
      """
         Test update a product with valid data.
         This operation should return a status code 200 and the updated product.
      """
      product = create_product(**self.product)
      payload: dict = {**self.product}
      payload.update({
          'name': 'Updated name',
          'category': category_serializers.CategorySerializer(product.category).data['name']
      })
      url = get_product_detail_url(name='private_product_detail', id=getattr(product, 'id'))
      response = self.client.put(url, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['name'], payload['name'])

   def test_try_to_update_product_with_invalid_data(self):
      """
         Try to update a product with invalid data.
         This operation should return a status code 400.
      """
      product = create_product(**self.product)
      payload: dict = {**self.product}
      payload.update({
          'unit_price': 'Not a number',
          'category': category_serializers.CategorySerializer(product.category).data['name']
      })
      url = get_product_detail_url(name='private_product_detail', id=getattr(product, 'id'))
      response = self.client.put(url, data=payload, format='json')
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

   def test_try_to_update_product_without_some_data(self):
      """
         Try to update a product without some data.
         This operation should return a status code 400.
      """
      product = create_product(**self.product)
      payload: dict = {**self.product}
      payload.update({
          'name': None,
          'category': category_serializers.CategorySerializer(product.category).data['name']
      })
      url = get_product_detail_url(name='private_product_detail', id=getattr(product, 'id'))
      response = self.client.put(url, data=payload, format='json')
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

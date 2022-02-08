from .dependencies_imports import *


class TestPublicRetrieveProductView(APITestCase):
   """ Tests for the retrieve product view """

   def test_retrieve_registered_product(self) -> None:
      """ Test retrieving a registered product """
      category = create_category(name='Test Category')
      product = create_product(category=category,
                               name='Test Product',
                               description='Test Description',
                               unit_price=10.0,
                               image_url='http://test.com/test.jpg',
                               offer=True,
                               discount_rate=10,
                               stok=10,
                               active=True)
      url = get_product_detail_url(name='public_product_detail', id=getattr(product, 'id'))
      response = self.client.get(url)
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data, serializers.ProductSerializer(product).data)

   def test_try_to_retrieve_unregistered_product(self) -> None:
      """ Test try retrieving an unregistered product """
      category = create_category(name='Test Category')
      product = create_product(category=category,
                               name='Test Product',
                               description='Test Description',
                               unit_price=10.0,
                               image_url='http://test.com/test.jpg',
                               offer=True,
                               discount_rate=10,
                               stok=10,
                               active=True)
      url = get_product_detail_url(name='public_product_detail', id=0)
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

   def test_try_to_retrieve_inactive_product(self) -> None:
      """ Test try retrieving an inactive product """
      category = create_category(name='Test Category')
      product = create_product(category=category,
                               name='Test Product',
                               description='Test Description',
                               unit_price=10.0,
                               image_url='http://test.com/test.jpg',
                               offer=True,
                               discount_rate=10,
                               stok=10,
                               active=False)
      url = get_product_detail_url(name='public_product_detail', id=getattr(product, 'id'))
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
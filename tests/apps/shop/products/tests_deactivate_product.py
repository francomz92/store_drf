from .dependencies_imports import *

product_payload: Dict[str, Any] = {
    'description': 'description 1',
    'unit_price': 1.0,
    'stok': 10,
    'image_url': None,
    'offer': True,
    'discount_rate': 10,
}


class TestPublicDeactivateProductView(APITestCase):

   def setUp(self) -> None:
      category = category_models.Category.objects.get_or_create(name='Some Category')[0]
      self.product = create_product(category=category, **product_payload)
      return super().setUp()

   def test_try_to_deactivate_product_without_authentication(self):
      """
         Try to deactivate a product without authentication.
         This operation should return a 401 error.
      """
      url = get_product_detail_url(name='private_product_detail', id=getattr(self.product, 'id'))
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateDeactivateProductView(APITestCase):

   def setUp(self) -> None:
      user = get_or_create_user(email='root@email.com', dni='12345678', password='root_password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      category = category_models.Category.objects.get_or_create(name='Some Category')[0]
      self.product = create_product(category=category, **product_payload)
      return super().setUp()

   def test_deactivate_registered_product_with_authentication(self):
      """
         Test deactivate a product with authentication.
         This operation should return a status code 204 and turn false product active property status.
      """
      url = get_product_detail_url(name='private_product_detail', id=getattr(self.product, 'id'))
      response = self.client.delete(url)
      deactivated_product = models.Product.objects.filter(id=getattr(self.product, 'id')).first()
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertFalse(getattr(deactivated_product, 'active'))

   def test_try_to_deactivate_no_registered_product(self):
      """
         Try to deactivate a no registered product.
         This operation should return a status code 404.
      """
      url = get_product_detail_url(name='private_product_detail', id=0)
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
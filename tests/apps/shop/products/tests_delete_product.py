from .dependencies_imports import *

product_payload: Dict[str, Any] = {
    'description': 'description 1',
    'unit_price': 1.0,
    'stok': 10,
    'image_url': None,
    'offer': True,
    'discount_rate': 10,
}


class TestPublicDeleteProductView(APITestCase):

   def setUp(self) -> None:
      category = category_models.Category.objects.get_or_create(name='Some Category')[0]
      self.product = create_product(category=category, **product_payload)
      return super().setUp()

   def test_try_to_delete_product_without_authentication(self):
      """
         Try to delete a product without authentication.
         This operation should return a 401 error.
      """
      url = get_product_detail_url(name='private_product_delete', id=getattr(self.product, 'id'))
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateDeleteProductView(APITestCase):

   def setUp(self) -> None:
      user = get_or_create_user(email='root@email.com', dni='12345678', password='root_password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      category = category_models.Category.objects.get_or_create(name='Some Category')[0]
      self.product = create_product(category=category, **product_payload)
      return super().setUp()

   def test_delete_registered_product_with_authentication(self):
      """
         Test delete a product with authentication.
         This operation should return a status code 204 and turn false product active property status.
      """
      url = get_product_detail_url(name='private_product_delete', id=getattr(self.product, 'id'))
      response = self.client.delete(url)
      deleted_product = models.Product.objects.filter(id=getattr(self.product, 'id')).first()
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertIsNone(deleted_product)

   def test_try_to_delete_no_registered_product(self):
      """
         Try to delete a no registered product.
         This operation should return a status code 404.
      """
      url = get_product_detail_url(name='private_product_delete', id=0)
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
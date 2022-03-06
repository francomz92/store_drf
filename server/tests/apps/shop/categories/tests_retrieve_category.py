from .dependencies_imports import *


class ShopCategoriesRetrieveViewTest(APITestCase):

   def setUp(self) -> None:
      user = get_or_create_user(email='email@test.com', dni='22222222', password='password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_retrieve_category(self):
      """
         Retrieve category.
         This operation should return an status code 200, a category and create category.
      """
      category = create_category('Category')
      response = self.client.get(get_category_detail_url(category.__getattribute__('id')))
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['name'], category.__getattribute__('name'))

   def test_try_to_retrieve_a_category_that_does_not_exist(self):
      """
         Try to retrieve a category that does not exist.
         This operation should return an status code 404 and does not retrieve a category.
      """
      response = self.client.get(get_category_detail_url(0))
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
      self.assertIn('detail', data)
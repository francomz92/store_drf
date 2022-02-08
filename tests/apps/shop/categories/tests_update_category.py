from .dependencies_imports import *


class ShopCategoryUpdateViewTest(APITestCase):

   def setUp(self) -> None:
      user = get_or_create_user(email='email@test.com', dni='22222222', password='password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_update_category(self):
      """
       Update an existing category.
       This operation should return an status code 200, update the category and return this.
      """
      category = create_category('Category')
      response = self.client.put(get_category_detail_url(category.__getattribute__('id')),
                                 data={'name': 'Updated Category'},
                                 format='json')
      data = response.json()
      updated_category = Category.objects.filter(name='Updated Category').first()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(serializers.CategorySerializer(updated_category).data, data)

   def test_try_to_update_a_category_that_does_not_exist(self):
      """
         Try to update a category that does not exist.
         This operation should return an status code 404 and does not update a category.
      """
      response = self.client.put(get_category_detail_url(0), data={'name': 'Updated Category'}, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
      self.assertIn('detail', data)

   def test_try_to_update_a_category_with_invalid_data(self):
      """
         Try to update a category with invalid data.
         This operation should return an status code 400 and does not update a category.
      """
      category = create_category('Category')
      response = self.client.put(get_category_detail_url(category.__getattribute__('id')),
                                 data={'name': ''},
                                 format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIn('name', data)
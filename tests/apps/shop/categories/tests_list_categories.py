from .dependencies_imports import *

CATEGORY_URL = reverse_lazy('shop:categories:categories')

class ShopCategoriesListViewTest(APITestCase):

   QUANTITY_OF_CATEGORIES_TO_CREATE = 3

   def setUp(self) -> None:
      user = get_or_create_user(email='email@test.com', dni='22222222', password='password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_get_list_categories(self):
      """
         Get list of categories.
         This operation should return an status code 200 and a list of categories.
      """
      for i in range(self.QUANTITY_OF_CATEGORIES_TO_CREATE):
         create_category(f'Category {i}')
      response = self.client.get(CATEGORY_URL)
      data = response.json()
      categories = Category.objects.all()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(data['results']), self.QUANTITY_OF_CATEGORIES_TO_CREATE)
      self.assertEqual(data['results'], serializers.CategorySerializer(categories, many=True).data)

   def test_get_category_by_search_name_query_param(self):
      """
         Get category by name query param.
         This operation should return an status code 200 and a list of categories that matches with the provided name.
      """
      name = 'Category'
      for i in range(self.QUANTITY_OF_CATEGORIES_TO_CREATE):
         create_category(f'{name}_{i}')
      response = self.client.get(f'{CATEGORY_URL}?search={name}_1')
      data = response.json()
      categories = Category.objects.filter(name=f'{name}_1')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(serializers.CategorySerializer(categories, many=True).data, data['results'])

   def test_try_to_get_category_by_search_name_no_registered_query_param(self):
      """
         Try to get category by search name no registered query param.
         This operation should return an status code 200 and a empty list.
      """
      create_category('Category')
      response = self.client.get(f'{CATEGORY_URL}?search=non_registered_category')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])

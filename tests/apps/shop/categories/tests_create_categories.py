from .dependencies_imports import *


class ShopCategoriesCreateViewTest(APITestCase):

   def setUp(self) -> None:
      user = get_or_create_user(email='email@test.com', dni='22222222', password='password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_create_category_with_valid_data(self):
      """
         Ccreate category with valid data.
         This operation should return an status code 201, a new category and create a new category.
      """
      payload: Dict[str, str] = {'name': 'New Category'}
      response = self.client.post(CATEGORY_URL, data=payload, format='json')
      data = response.json()
      new_category = Category.objects.filter(name=payload['name']).first()
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(data['name'], payload['name'])
      self.assertIsNotNone(new_category)
      self.assertEqual(new_category.__getattribute__('name'), payload['name'])

   def test_try_to_create_a_new_category_without_some_required_data(self):
      """
         Try to create a new category without some required data.
         This operation should return an status code 400 and does not create a new category.
      """
      payload: Dict[str, str] = {}
      response = self.client.post(CATEGORY_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIn('name', data)

   def test_try_to_create_a_new_category_with_invalid_data(self):
      """
         Try to create a new category with invalid data.
         This operation should return an status code 400 and does not create a new category.
      """
      payload: Dict[str, str] = {'name': ''}
      response = self.client.post(CATEGORY_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIn('name', data)
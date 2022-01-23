from .imports import *


class ShopCategoriesDeleteViewTest(APITestCase):

   def setUp(self) -> None:
      user = get_or_create_user(email='email@test.com', dni='22222222', password='password')
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_delete_category(self):
      """
         Delete a category.
         This operation should return an status code 204 and delete the category.
      """
      category = create_category('Category')
      response = self.client.delete(get_category_detail_url(category.__getattribute__('id')))
      deleted_category = Category.objects.filter(name=category.__getattribute__('name')).first()
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertIsNone(deleted_category)
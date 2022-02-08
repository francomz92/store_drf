from .dependencies_imports import *


class LogInViewTests(APITestCase):

   payload: Dict[str, str] = {'email': 'test@example.com', 'dni': '12345671', 'password': 'test_password'}

   def setUp(self) -> None:
      get_or_create_user(self.payload['email'], self.payload['dni'], self.payload['password'])
      self.client = APIClient()
      return super().setUp()

   def test_login_with_valid_data(self):
      """
         Try to login with valid data.
         This operation should return a 200 status code, a message of welcome and token.
      """
      response = self.client.post(LOGIN_URL, data=self.payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn('message', data)
      self.assertIn('access', data)
      self.assertIn('refresh', data)

   def test_login_with_invalid_data(self):
      """
         Try to login with invalid data.
         This operation should return a 400 status code, a message of invalid credentials and does not create a new token.
      """
      payload: Dict[str, str] = {**self.payload}
      payload['password'] = 'test_password_different'
      response = self.client.post(LOGIN_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
      self.assertNotIn('access', data)
      self.assertNotIn('refresh', data)

   def test_try_to_login_without_some_required_data(self):
      """
         Try to login without some required data.
         This operation should return a 400 status code, the missing data and does not create a new token.
      """
      payload: Dict[str, str] = {'password': 'test_password'}
      response = self.client.post(LOGIN_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertNotIn('access', data)
      self.assertNotIn('refresh', data)
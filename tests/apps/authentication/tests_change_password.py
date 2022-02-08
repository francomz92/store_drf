from .dependencies_imports import *


class PasswordChangeViewTests(APITestCase):

   def setUp(self) -> None:
      user = User.objects.get_or_create({'email': 'test@changePassword.com', 'dni': '12345671'})[0]
      user.set_password('test_password')
      user.save()
      self.client = APIClient()
      self.client.force_authenticate(user=user)
      return super().setUp()

   def test_change_password_with_valid_data(self):
      """
         Try to change password with valid data.
         This operation should return a 200 status code, a message of confirmation and the new password.
      """
      payload: Dict[str, str] = {
          'old_password': 'test_password',
          'new_password': 'new_password',
          'confirm_password': 'new_password'
      }
      response = self.client.put(PASSWORD_CHANGE_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn('message', data)

   def test_try_to_change_password_with_invalid_data(self):
      """
         Try to change password with invalid data.
         This operation should return a 400 status code, a message of invalid credentials and does not change the password.
      """
      payload: Dict[str, str] = {
          'old_password': 'test_password_different',
          'new_password': 'new_password',
          'confirm_password': 'new_password'
      }
      response = self.client.put(PASSWORD_CHANGE_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertNotIn('new_password', data)

   def test_try_to_change_password_without_some_required_data(self):
      """
         Try to change password without some required data.
         This operation should return a 400 status code, the missing data and does not change the password.
      """
      payload: Dict[str, str] = {'new_password': 'new_password', 'confirm_password': 'new_password'}
      response = self.client.put(PASSWORD_CHANGE_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertNotIn('new_password', data)

   def test_try_to_change_password_with_invalid_confirm_password(self):
      """
         Try to change password with invalid confirm password.
         This operation should return a 400 status code, a message of invalid credentials and does not change the password.
      """
      payload: Dict[str, str] = {
          'old_password': 'test_password',
          'new_password': 'new_password',
          'confirm_password': 'new_password_different'
      }
      response = self.client.put(PASSWORD_CHANGE_URL, data=payload, format='json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertNotIn('new_password', data)
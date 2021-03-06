from .dependencies_imports import *

SIGNUP_URL = reverse_lazy('auth:signup')


class SignUpViewTests(APITestCase):

   payload: Dict[str, str] = {
       'email': 'test@example.com',
       'first_name': 'test name',
       'last_name': 'test_lastname',
       'province': 'test_province',
       'city': 'test_city',
       'zip_code': 'code',
       'dni': '12345678',
       'gender': 'M',
       'password': 'test_password',
       'password_confirmation': 'test_password',
   }

   def setUp(self) -> None:
      self.client = APIClient()
      return super().setUp()

   def test_successful_signup_with_valid_data(self):
      """
         Register successfully with valid data.
         This operation should return a 201 status code, a message of confirmation and created inactived user.
      """
      response = self.client.post(SIGNUP_URL, data=self.payload, format='json')
      data = response.json()
      user = User.objects.filter(email=self.payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertIn('message', data)
      self.assertIsNotNone(user)
      self.assertFalse(getattr(user, 'is_active'))

   def test_try_to_signup_without_some_required_data(self):
      """
         Try to register a new user without some required data.
         This operation should return a 400 status code, the missing data and does not create a new user.
      """
      payload: Dict[str, str] = {
          'email': 'test@example.com',
          'password': 'test_password',
          'password_confirmation': 'test_password',
      }
      response = self.client.post(SIGNUP_URL, data=payload, format='json')
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)

   def test_try_to_signup_with_distinct_passwords(self):
      """
         Try to register a new user with different passwords.
         This operation should return a 400 status code, the missing data and does not create a new user.
      """
      payload: Dict[str, str] = {**self.payload}
      payload['password_confirmation'] = 'test_password_different'
      response = self.client.post(SIGNUP_URL, data=payload, format='json')
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)

   def test_successful_account_activation(self):
      """
         Try to activate an account.
         This operation should return a 200 status code, a message of confirmation and activated user.
      """
      user_not_activated = create_an_user('email@example.com')
      url = get_account_activation_link(user_not_activated)
      response = self.client.get(url)
      data = response.json()
      user_activated = User.objects.filter(email=user_not_activated.__getattribute__('email')).first()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn('message', data)
      self.assertIsNotNone(user_activated)
      self.assertTrue(getattr(user_activated, 'is_active'))

from .dependencies_imports import *

LOGIN_URL = reverse_lazy('auth:login')
LOGOUT_URL = reverse_lazy('auth:logout')


class LogOutViewTests(APITestCase):

   payload: Dict[str, str] = {
       'email': 'test@email.com',
       'dni': '22222222',
       'password': 'test_password',
   }

   def setUp(self) -> None:
      self.user = get_or_create_user(self.payload['email'], self.payload['dni'], self.payload['password'])
      self.token = AccessToken.for_user(self.user)
      self.client = APIClient()
      self.client.credentials(HTTP_AUTHORIZATION='test ' + str(self.token))
      return super().setUp()

   def test_logout(self):
      login = self.client.post(LOGIN_URL,
                               data={
                                   'email': self.payload['email'],
                                   'password': self.payload['password']
                               },
                               format='json')
      login_response = login.json()
      response = self.client.post(LOGOUT_URL, data=login_response, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertFalse(check_token(self.user, login_response['access']))

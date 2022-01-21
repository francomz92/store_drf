from .imports import *


class LogOutViewTests(APITestCase):

   payload: Dict[str, str] = {
       'email': 'test@email.com',
       'dni': '22222222',
       'password': 'test_password',
   }

   def setUp(self) -> None:
      self.user = get_or_create_user(self.payload['email'], self.payload['dni'], self.payload['password'])
      token = AccessToken.for_user(self.user)
      self.client = APIClient()
      self.client.credentials(HTTP_AUTHORIZATION='test ' + str(token))
      return super().setUp()

   def test_logout(self):
      login = self.client.post(LOGIN_URL,
                               data={
                                   'email': self.payload['email'],
                                   'password': self.payload['password']
                               },
                               format='json')
      login_response = login.json()
      response = self.client.get(LOGOUT_URL)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertFalse(check_token(self.user, login_response['access']))

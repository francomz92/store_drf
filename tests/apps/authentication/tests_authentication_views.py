from typing import Dict
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator

from rest_framework_simplejwt.tokens import AccessToken

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from utils.auth import get_activation_account_link
from utils.tests.users import User, create_an_user, get_or_create_user

SIGNUP_URL = reverse_lazy('auth:signup')
LOGIN_URL = reverse_lazy('auth:login')
LOGOUT_URL = reverse_lazy('auth:logout')


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
      self.assertFalse(user.__getattribute__('is_active'))

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
      url = get_activation_account_link(user_not_activated)
      response = self.client.get(url)
      data = response.json()
      user_activated = User.objects.filter(email=user_not_activated.email).first()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn('message', data)
      self.assertIsNotNone(user_activated)
      self.assertTrue(user_activated.__getattribute__('is_active'))


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
      login = self.client.post(LOGIN_URL,
                               data={
                                   'email': self.payload['email'],
                                   'password': self.payload['password']
                               },
                               format='json')

      self.login_response = login.json()
      return super().setUp()

   def test_logout(self):
      response = self.client.get(LOGOUT_URL)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertFalse(default_token_generator.check_token(self.user, self.login_response['refresh']))
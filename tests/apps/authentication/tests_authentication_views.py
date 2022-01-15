from typing import Dict
import json
from django.urls import reverse_lazy
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ...utils.users import User

SIGNUP_URL = reverse_lazy('auth:signup')


class SignUpViewTests(APITestCase):

   def setUp(self) -> None:
      self.client = APIClient()
      return super().setUp()

   def test_successful_signup_with_valid_data(self):
      """
         Register successfully with valid data.
         This operation should return a 201 status code, a message of confirmation and created inactived user.
      """
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
      response = self.client.post(SIGNUP_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
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
      response = self.client.post(SIGNUP_URL, data=json.dumps(payload), content_type='application/json')
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)

   def test_try_to_signup_with_distinct_passwords(self):
      """
         Try to register a new user with different passwords.
         This operation should return a 400 status code, the missing data and does not create a new user.
      """
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
          'password_confirmation': 'different_password',
      }
      response = self.client.post(SIGNUP_URL, data=json.dumps(payload), content_type='application/json')
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)

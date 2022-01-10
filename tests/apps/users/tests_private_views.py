import os
import json
from typing import Dict
from django.http import response
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from apps.users import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
USER_URL = str(os.getenv('DOMAIN')) + '/api/users/'
SUPERUSER = User.objects.get_or_create(email='root@example.com')[0]
setattr(SUPERUSER, 'is_staff', True)


def create_an_user(email: str):
   return User.objects.create(first_name='pepe',
                              email=email,
                              last_name='abc',
                              province='Chaco',
                              city='Juan Jose Castelli',
                              gender='M',
                              zip_code='3705')


class UserGeneralViewsTest(APITestCase):

   def setUp(self) -> None:
      self.client = APIClient()
      self.client.force_authenticate(SUPERUSER)
      return super().setUp()

   def test_json_response_with_user_list(self):
      """
         Return a json response with a list of users when visit user resource.
      """
      create_an_user('pepe@example.com')
      response = self.client.get(USER_URL)
      data = response.json()
      users = User.objects.all()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertCountEqual(data['results'], serializers.UsersListSerializer(users, many=True).data)

   def test_create_successfull_user(self):
      """
         Create a new user successfully.
      """
      payload: Dict[str, str] = {
          "email": "pepto@email.com",
          "password": "pepe1234",
          "first_name": "Jose",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertIsNotNone(user)
      self.assertEqual(data, serializers.UsersListSerializer(user).data)

   def test_try_create_user_without_any_required_field(self):
      """
         Try to create a user without any required fields.
         This operation should return an error and user should not be created.
      """
      payload: Dict[str, str] = {
          # _first_name field is required
          "email": "pepto@email.com",
          "password": "pepe1234",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)
      self.assertIn('first_name', data)

   def test_try_create_user_with_registered_email(self):
      """
         Try to create a user with a registered email address.
         This operation should return an error and user should not be created.
      """
      create_an_user('pepe123@email.com')
      payload: Dict[str, str] = {
          "email": "pepe123@email.com",
          "password": "pepe1234",
          "first_name": "Jose",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIn('email', data)

   def test_try_create_user_with_field_character_limit_exceeded(self):
      """
         Try to create a user with _first_name field character limit exceeded.
         This operation should return an error and user should not be created.
      """
      payload: Dict[str, str] = {
          "email": "pepe123@email.com",
          "password": "pepe1234",
          "first_name": "Lorem ipsum dolor sit amet, consectetur porttitor as",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)
      self.assertIn('first_name', data)

   def test_successful_get_user_with_email_contains_query_param(self):
      """
         Get successfully user data when email query parameter is specified
      """
      user = create_an_user('user@example.com')
      response = self.client.get(USER_URL + '?email=userexample')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIsNotNone(data)
      self.assertIn(serializers.UsersListSerializer(user).data, data['results'])

   def test_try_get_user_by_id_email_not_registered_query_param(self):
      """
         Try get user data when id non-existing path parameter is specified
         This operation should return an empty list
      """
      response = self.client.get(USER_URL + '?email=email_not_registered@example.com')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])

   def test_successful_get_user_by_province_query_param(self):
      """
         Get successfully user data when province query parameter is specified
      """
      user = create_an_user('user@example.com')
      response = self.client.get(USER_URL + '?province=Chaco')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIsNotNone(data)
      self.assertIn(serializers.UsersListSerializer(user).data, data['results'])

   def test_try_get_user_by_province_not_registered_query_param(self):
      """
         Get successfully user data when province not registered queryy parameter is specified
      """
      response = self.client.get(USER_URL + '?province=NotProvince')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])


# class UserParticularViewsTest(APITestCase):

#    def setUp(self) -> None:
#       self.client = APIClient()
#       self.client.force_authenticate(SUPERUSER)
#       return super().setUp()

#    def test_get_user_by_id_path_param(self):
#       """
#          Get user data when id path parameter is specified
#       """
#       response = self.client.get(USER_URL + '/1')
#       data = response.json()
#       self.assertEqual(response.status_code, status.HTTP_200_OK)
#       self.assertEqual(data['email'], SUPERUSER.email)

#    def test_try_get_user_not_registered_by_id_path_param(self):
#       """
#          Try get user data when id non-existing path parameter is specified
#          This operation should return an error 404 not found
#       """
#       response = self.client.get(USER_URL + '/999')
#       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

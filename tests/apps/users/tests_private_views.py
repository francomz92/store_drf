import json
from typing import Dict
from django.urls import reverse_lazy
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from tests.utils.users import User, SUPERUSER, create_an_user
from apps.users import serializers

USER_URL = reverse_lazy('users:users_list_create')


class UserGeneralViewsTest(APITestCase):

   def setUp(self) -> None:
      self.client = APIClient()
      self.client.force_authenticate(SUPERUSER)
      return super().setUp()

   def test_get_users_list(self):
      """
         Return a json response with a list of users when visit user resource.
      """
      create_an_user('pepe@example.com')
      response = self.client.get(USER_URL)
      data = response.json()
      users = User.objects.all()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertCountEqual(data['results'], serializers.UsersListSerializer(users, many=True).data)

   def test_create_user_with_valid_required_data(self):
      """
         Create a new user successfully when provided data is valid
      """
      payload: Dict[str, str] = {
          "email": "pepto@email.com",
          "first_name": "Jose",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
          'dni': '12314313',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertIsNotNone(user)
      self.assertEqual(data, serializers.UsersListSerializer(user).data)

   def test_try_to_create_user_without_any_required_field(self):
      """
         Try to create a user without any required fields.
         This operation should return an error and user should not be created.
      """
      payload: Dict[str, str] = {
          # _first_name field is required
          "email": "pepto@email.com",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
          'dni': '12314312',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)
      self.assertIn('first_name', data)

   def test_try_to_create_user_with_registered_email(self):
      """
         Try to create a user with a registered email address.
         This operation should return an error and user should not be created.
      """
      create_an_user('pepe123@email.com')
      payload: Dict[str, str] = {
          "email": "pepe123@email.com",
          "first_name": "Jose",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
          'dni': '12314312',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIn('email', data)

   def test_try_to_create_user_with_field_character_limit_exceeded(self):
      """
         Try to create a user with _first_name field character limit exceeded.
         This operation should return an error and user should not be created.
      """
      payload: Dict[str, str] = {
          "email": "pepe123@email.com",
          "first_name": "Lorem ipsum dolor sit amet, consectetur porttitor as",
          "last_name": "Argento",
          "province": "Buenos Aires",
          "city": "Capital",
          "gender": "M",
          'zip_code': '3705',
          'dni': '12314312',
      }
      response = self.client.post(USER_URL, data=json.dumps(payload), content_type='application/json')
      data = response.json()
      user = User.objects.filter(email=payload['email']).first()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIsNone(user)
      self.assertIn('first_name', data)

   def test_get_user_with_email_contains_query_param(self):
      """
         Get successfully user data when email query parameter is specified
      """
      user = create_an_user('user@example.com')
      response = self.client.get(USER_URL + '?email=userexample')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIsNotNone(data)
      self.assertIn(serializers.UsersListSerializer(user).data, data['results'])

   def test_try_to_get_user_by_id_email_not_registered_query_param(self):
      """
         Try to get user data when id non-existing path parameter is specified
         This operation should return an empty list
      """
      response = self.client.get(USER_URL + '?email=email_not_registered@example.com')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])

   def test_get_user_by_province_query_param(self):
      """
         Get successfully users data when province query parameter is specified
      """
      user = create_an_user('user@example.com')
      response = self.client.get(USER_URL + '?province=Chaco')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIsNotNone(data)
      self.assertIn(serializers.UsersListSerializer(user).data, data['results'])

   def test_get_user_by_province_not_registered_query_param(self):
      """
         Try to get users data when province not registered queryy parameter is specified.
         This operation should return an empty list
      """
      response = self.client.get(USER_URL + '?province=NotProvince')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['results'], [])

   def test_to_get_searched_user_by_query_param(self):
      """
         Try to get users data when search param is specified (email, first_name or last_name).
      """
      user = create_an_user('email@example.com')
      response = self.client.get(USER_URL + '?search=' + user.email)
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn(serializers.UserSingleSerializer(user).data, data['results'])


class UserParticularViewsTest(APITestCase):

   def setUp(self) -> None:
      self.client = APIClient()
      self.client.force_authenticate(SUPERUSER)
      return super().setUp()

   def test_get_user_by_id_path_param(self):
      """
         Get user data when id path parameter is specified
      """
      user = create_an_user('user@example.com')
      response = self.client.get(reverse_lazy('users:single_user', args=(user.id, )))
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['email'], user.email)

   def test_try_to_get_user_not_registered_by_id_path_param(self):
      """
         Try get user data when id non-existing path parameter is specified
         This operation should return an error 404 not found
      """
      response = self.client.get(reverse_lazy('users:single_user', args=(999, )))
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
      self.assertNotIn('email', data)

   def test_update_registered_user(self):
      """
         Update registered user.
         This operation should return the same user with the new data provided
      """
      user = create_an_user('user@example.com', first_name='example', last_name='Example')
      payload = serializers.UserSingleSerializer(user).data
      payload['first_name'] = "Lorem"
      response = self.client.put(reverse_lazy('users:single_user', args=(user.id, )),
                                 data=json.dumps(payload),
                                 content_type='application/json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(data['first_name'], payload['first_name'])

   def test_try_to_update_user_with_invalid_data(self):
      """
         Try update user with invalid data, for example without an required field or invalid field value.
         This operation should return an error 400 Bad Request and doesn't update the user
      """
      user = create_an_user('user@example.com', first_name='example', last_name='Example')
      payload: Dict[str, str] = {
          "first_name": "Lorem asdasdasdajhj ahsdiola hasd oiahsdoja idaa asdjia aji",
      }
      response = self.client.put(reverse_lazy('users:single_user', args=(user.id, )),
                                 data=json.dumps(payload),
                                 content_type='application/json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertNotEqual(data, serializers.UserSingleSerializer(user).data)

   def test_try_to_update_an_illegal_field(self):
      """
         Try to update user illegal data, for example email.
         This operation should return user data without updated email
      """
      user = create_an_user('user@example.com', first_name='example', last_name='Example')
      payload = serializers.UserSingleSerializer(user).data
      payload['email'] = 'new@example.com'
      response = self.client.put(reverse_lazy('users:single_user', args=(user.id, )),
                                 data=json.dumps(payload),
                                 content_type='application/json')
      data = response.json()
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertNotEqual(data['email'], payload['email'])
from typing import Dict

from django.urls import reverse_lazy

from rest_framework_simplejwt.tokens import AccessToken

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from utils.auth import get_account_activation_link, check_token
from utils.tests.users import User, create_an_user, get_or_create_user

SIGNUP_URL = reverse_lazy('auth:signup')
LOGIN_URL = reverse_lazy('auth:login')
LOGOUT_URL = reverse_lazy('auth:logout')
PASSWORD_CHANGE_URL = reverse_lazy('auth:password_change')

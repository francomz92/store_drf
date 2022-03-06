from typing import Dict

from django.urls import reverse_lazy

from rest_framework_simplejwt.tokens import AccessToken

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from utils.auth import get_account_activation_link, check_token
from utils.tests.users import User, create_an_user, get_or_create_user

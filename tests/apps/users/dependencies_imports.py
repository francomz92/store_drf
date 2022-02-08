import json
from typing import Dict

from django.urls import reverse_lazy

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from utils.tests.users import User, SUPERUSER, create_an_user, get_or_create_user
from apps.users import serializers
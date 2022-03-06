from typing import Dict

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from utils.tests.users import get_or_create_user
from utils.tests.categories import (
    create_category,
    get_category_detail_url,
    Category,
    reverse_lazy,
)

from apps.shop.categories import serializers
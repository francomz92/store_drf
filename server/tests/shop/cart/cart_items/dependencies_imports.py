from typing import Dict, Any

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from utils.tests.users import get_or_create_user
from utils.tests.categories import create_category
from utils.tests.products import create_product
from utils.tests.cart import get_cart_item_url, create_cart_item, cart_models, reverse_lazy

from apps.shop.categories import serializers as category_serializers
from apps.shop.products import serializers as product_serializers
from apps.shop.cart import serializers

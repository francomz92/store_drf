import mock

from typing import Dict, Type, Any

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from utils.tests.users import get_or_create_user
from utils.tests.categories import create_category
from utils.tests.products import (
    create_product,
    get_products,
    get_product_detail_url,
    reverse_lazy,
)

from apps.shop.products import models, serializers
from apps.shop.categories import models as category_models, serializers as category_serializers

# def mock_category(name: str) -> Dict:
#    category = mock.Mock(spec=category_models.Category)
#    category._state = mock.Mock()
#    category.name = name
#    return category

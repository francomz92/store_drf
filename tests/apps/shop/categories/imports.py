from typing import Dict

from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from utils.tests.users import get_or_create_user
from apps.shop.categories import models, serializers

Category = models.Category

CATEGORY_URL = reverse_lazy('shop:categories:categories')


def create_category(name: str) -> Category:
   return Category.objects.create(name=name)


def get_category_detail_url(id: int) -> str:
   return reverse_lazy('shop:categories:category_detail', kwargs={'id': id})
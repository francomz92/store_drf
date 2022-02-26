from typing import TypeVar, Type

from django.db.models.query import QuerySet
from django.db import models

from django.urls import reverse_lazy
from django.utils.crypto import get_random_string

from apps.shop.products import models as product_models
from apps.shop.categories import models as category_models

_T = TypeVar("_T", bound=models.Model, covariant=True)


def get_product_detail_url(name: str, id: int) -> str:
   return reverse_lazy(f'shop:products:{name}', kwargs={'id': id})


def create_product(category: category_models.Category,
                   *,
                   name: str = get_random_string(length=8),
                   description: str,
                   unit_price: float,
                   image_url: str = None,
                   offer: bool = None,
                   discount_rate: int = None,
                   stok: int,
                   active: bool = True) -> product_models.Product:
   return product_models.Product.objects.create(category=category,
                                                name=name,
                                                description=description,
                                                unit_price=unit_price,
                                                stok=stok,
                                                image_url=image_url,
                                                offer=offer,
                                                discount_rate=discount_rate,
                                                active=active)


def get_products(**kwargs) -> QuerySet[_T]:
   """ Get a list of filtered products """
   return product_models.Product.objects.filter(**kwargs)

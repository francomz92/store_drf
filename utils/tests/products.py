from typing import TypeVar, Type

from django.db.models.query import QuerySet
from django.db import models

from django.urls import reverse_lazy
from django.utils.crypto import get_random_string

from apps.shop.products import models as product_models
from apps.shop.categories import models as category_models

_T = TypeVar("_T", bound=models.Model, covariant=True)

PUBLIC_PRODUCTS_URL = reverse_lazy('shop:products:public_products')
PRIVATE_PRODUCTS_URL = reverse_lazy('shop:products:private_products')


def get_product_detail_url(id: int) -> str:
   return reverse_lazy('shop:products:product_detail', kwargs={'id': id})


def create_product(category: Type[category_models.Category],
                   *,
                   name: str = None,
                   description: str,
                   unit_price: float,
                   image_url: str = None,
                   offer: bool = None,
                   discount_rate: int = None,
                   stok: int,
                   active: bool = True) -> Type[product_models.Product]:
   return product_models.Product.objects.create(category=category,
                                                name=name or get_random_string(length=8),
                                                description=description,
                                                unit_price=unit_price,
                                                stok=stok,
                                                image_url=image_url,
                                                offer=offer,
                                                discount_rate=discount_rate,
                                                active=active)


def get_products(**kwargs) -> QuerySet[_T]:
   """ Get a list of filtered products """
   products = product_models.Product.objects.filter(**kwargs)
   return products

from typing import TypeVar, Type

from django.db.models.query import QuerySet
from django.db import models

from django.urls import reverse_lazy

from apps.shop.products import models as product_models
from apps.shop.cart import models as cart_models

_T = TypeVar('_T', bound=models.Model, covariant=True)


def get_cart_item_url(name: str, **kwargs) -> str:
   return reverse_lazy(f'shop:cart:{name}', kwargs=kwargs)


def create_cart_item(cart: product_models.Product,
                     product: product_models.Product,
                     ammount: int = 1) -> cart_models.CartItem:
   return cart_models.CartItem.objects.create(cart=cart, product=product, ammount=ammount)

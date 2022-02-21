from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Cart, CartItem
from apps.shop.products.models import Product


@receiver(signal=post_save, sender=CartItem)
def cart_item_post_save(sender, instance, created, **kwargs):
   instance.cart.save()


@receiver(signal=post_delete, sender=CartItem)
def cart_item_post_delete(sender, instance, **kwargs):
   instance.cart.save()

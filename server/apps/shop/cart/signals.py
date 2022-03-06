import threading

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import CartItem


@receiver(signal=post_save, sender=CartItem)
def cart_item_post_save(sender, instance, created, **kwargs):
   # thread = threading.Thread(target=instance.cart.save, daemon=True)
   # thread.start()
   instance.cart.save()


@receiver(signal=post_delete, sender=CartItem)
def cart_item_post_delete(sender, instance, **kwargs):
   # thread = threading.Thread(target=instance.cart.save, daemon=True)
   # thread.start()
   instance.cart.save()
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Product


@receiver(signal=post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
   for item in instance.product_item.all():
      if item.product == instance:
         item.save()

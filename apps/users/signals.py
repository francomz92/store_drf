from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from apps.shop.cart.models import Cart


@receiver(signal=post_save, sender=get_user_model())
def user_post_save(sender, instance, created, **kwargs):
   if created:
      Cart.objects.create(user=instance)
   instance.user_cart.save()

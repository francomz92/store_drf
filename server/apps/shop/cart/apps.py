from django.apps import AppConfig


class CartConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'apps.shop.cart'

   def ready(self) -> None:
      import apps.users.signals
      import apps.shop.products.signals
      return super().ready()

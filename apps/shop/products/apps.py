from django.apps import AppConfig


class ProductsConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'apps.shop.products'

   def ready(self) -> None:
      import apps.shop.cart.signals
      return super().ready()

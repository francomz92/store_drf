from django.contrib.auth import get_user_model

from core.models import models, GenericModel, validators, _


class Cart(GenericModel):
   user = models.OneToOneField(verbose_name=_('User'),
                               to=get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='user_cart')
   total = models.DecimalField(verbose_name=_('Total'),
                               max_digits=8,
                               decimal_places=2,
                               default=0,
                               editable=False)

   class Meta:
      verbose_name = _('Cart')
      verbose_name_plural = _('Carts')

   def __str__(self) -> str:
      return f'{getattr(self.user, "first_name")}\'s Cart'

   def _set_total(self):
      self.total = 0
      if getattr(self, 'cart_items').all().exists():
         for item_product in getattr(self, 'cart_items').all():
            self.total += item_product.price

   def clean(self) -> None:
      self._set_total()
      return super().clean()

   def save(self, *args, **kwargs) -> None:
      self.clean()
      return super().save(*args, **kwargs)


class CartItem(GenericModel):
   cart = models.ForeignKey(verbose_name=_('Cart'),
                            to='cart.Cart',
                            on_delete=models.CASCADE,
                            related_name='cart_items')
   product = models.ForeignKey(verbose_name=_('Product'),
                               to='products.Product',
                               on_delete=models.CASCADE,
                               related_name='product_item')
   ammount = models.PositiveSmallIntegerField(verbose_name=_('Ammount'),
                                              validators=[validators.MinValueValidator(1)])
   price = models.DecimalField(verbose_name=_('Price'),
                               max_digits=8,
                               decimal_places=2,
                               default=0,
                               editable=False)

   class Meta:
      verbose_name = _('Cart Item')
      verbose_name_plural = _('Cart Items')
      ordering = ('cart', )

   def __str__(self) -> str:
      return f'{getattr(self.product, "name")}: {self.ammount}'

   def _set_price(self):
      self.price = getattr(self.product, 'price_with_discount') * self.ammount

   def clean(self) -> None:
      self._set_price()
      return super().clean()

   def save(self, *args, **kwargs) -> None:
      self.clean()
      return super().save(*args, **kwargs)

   @classmethod
   def get_total_price(cls, cart_items: list) -> tuple:
      total = 0
      total_without_discount = 0
      for item in cart_items:
         total += float(item['price'])
         total_without_discount += float(item['product']['unit_price']) * float(item['ammount'])
      return total, total_without_discount
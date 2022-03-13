from django.contrib.auth import get_user_model

from core.models import models, GenericModel, validators, _


class Order(GenericModel):
   """ Order model """

   user = models.ForeignKey(verbose_name=_('User'),
                            to=get_user_model(),
                            on_delete=models.CASCADE,
                            related_name='orders')
   total = models.DecimalField(verbose_name=_('Total'),
                               max_digits=10,
                               decimal_places=2,
                               validators=(validators.MinValueValidator(0), ))

   class Meta:
      verbose_name = _('Order')
      verbose_name_plural = _('Orders')
      ordering = ('-created_at', )

   def __str__(self):
      return f'Order {getattr(self, "id")}'


class OrderItem(GenericModel):
   """ OrderItems model """

   order = models.ForeignKey(verbose_name=_('Order'),
                             to=Order,
                             on_delete=models.CASCADE,
                             related_name='items_order')
   product = models.CharField(verbose_name=_('Product'), max_length=255)
   ammount = models.PositiveSmallIntegerField(verbose_name=_('Ammount'),
                                              validators=(validators.MinValueValidator(1), ))
   price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)

   class Meta:
      verbose_name = _('OrderItem')
      verbose_name_plural = _('Order Items')

   def __str__(self):
      return f'OrderItem {getattr(self, "id")}'
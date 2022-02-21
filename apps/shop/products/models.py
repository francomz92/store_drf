from core.models import GenericModel, models, _


class Product(GenericModel):
   category = models.ForeignKey(verbose_name=_('Category'),
                                to='categories.Category',
                                on_delete=models.PROTECT,
                                related_name='category')
   name = models.CharField(verbose_name=_('Name'), max_length=100)
   description = models.TextField(verbose_name=_('Description'), max_length=500)
   unit_price = models.DecimalField(verbose_name=_('Unit Price'), max_digits=8, decimal_places=2)
   image_url = models.ImageField(verbose_name=_('Image'), upload_to='products/images/', null=True, blank=True)
   offer = models.BooleanField(verbose_name=_('On sale'), default=False)
   discount_rate = models.PositiveSmallIntegerField(verbose_name=_('Discount Rate'), default=0)
   price_with_discount = models.DecimalField(verbose_name=_('Price with discount'),
                                             max_digits=8,
                                             decimal_places=2,
                                             default=0,
                                             editable=False)
   stok = models.PositiveIntegerField(verbose_name=_('Stock'))
   active = models.BooleanField(verbose_name=_('Active'), default=True)

   class Meta:
      verbose_name = _('Product')
      verbose_name_plural = _('Products')
      ordering = ('offer', )

   def on_sale(self):
      return self.offer

   def _set_price(self):
      self.price_with_discount = self.unit_price
      if self.on_sale():
         self.price_with_discount = self.unit_price - (self.unit_price * self.discount_rate / 100)

   def _check_active(self):
      if self.stok <= 1:
         self.active = False

   def clean(self) -> None:
      self._set_price()
      self._check_active()
      return super().clean()

   def save(self, *args, **kwargs):
      self.clean()
      super().save(*args, **kwargs)

   def __str__(self):
      return self.name

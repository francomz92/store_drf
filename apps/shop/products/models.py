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
   offer = models.BooleanField(verbose_name=_('Offer'), default=False)
   discount_rate = models.PositiveSmallIntegerField(verbose_name=_('Discount Rate'), default=0)
   stok = models.PositiveIntegerField(verbose_name=_('Stock'))
   active = models.BooleanField(verbose_name=_('Active'), default=True)

   class Meta:
      verbose_name = _('Product')
      verbose_name_plural = _('Products')
      ordering = ('offer', )

   def on_sale(self):
      return self.offer

   def get_price(self):
      if self.on_sale():
         return self.unit_price - (self.unit_price * self.discount_rate / 100)
      return self.unit_price

   def _check_active(self):
      if self.stok <= 1:
         self.active = False

   def save(self, *args, **kwargs):
      self._check_active()
      super().save(*args, **kwargs)

   def __str__(self):
      return self.name

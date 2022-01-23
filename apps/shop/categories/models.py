from core.models import GenericModel, models, _


class Category(GenericModel):
   name = models.CharField(verbose_name=_('Name'), max_length=100)

   class Meta:
      verbose_name = _('Category')
      verbose_name_plural = _('Categories')

   def __str__(self):
      return self.name

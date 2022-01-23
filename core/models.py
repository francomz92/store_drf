from django.db import models
from django.utils.translation import gettext as _


class GenericModel(models.Model):
   created_at = models.DateTimeField(verbose_name=_('Create At'), auto_now_add=True)
   updated_at = models.DateTimeField(verbose_name=_('Create At'), auto_now=True)

   class Meta:
      abstract = True
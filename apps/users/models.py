from typing import Optional

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from core.models import GenericModel, models, _


class UserManager(BaseUserManager):

   def create(self, email: str, password: Optional[str] = None, **kwargs):
      user = self.model(
          email=self.normalize_email(email),
          **kwargs,
      )
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_user(self, email: str, password: Optional[str] = None):
      return self.create(email, password)

   def create_superuser(self,
                        email: str,
                        dni: str,
                        password: Optional[str] = None,
                        is_superuser: Optional[bool] = True):
      return self.create(email, password, dni=dni, is_superuser=is_superuser, is_staff=True, is_active=True)


class User(AbstractBaseUser, PermissionsMixin, GenericModel):
   first_name = models.CharField(verbose_name=_('Name'), max_length=50)
   last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
   province = models.CharField(verbose_name=_('Provincia'), max_length=50)
   city = models.CharField(verbose_name=_('City'), max_length=50)
   zip_code = models.CharField(verbose_name=_('Zip Code'), max_length=8)
   email = models.EmailField(verbose_name=_('Email'), max_length=128, unique=True)
   dni = models.CharField(verbose_name='DNI', max_length=8, unique=True)
   gender = models.CharField(verbose_name='Gender',
                             max_length=1,
                             choices=(
                                 ('M', _('Male')),
                                 ('F', _('Female')),
                                 ('O', _('Other')),
                             ))
   is_staff = models.BooleanField(verbose_name='Staff', default=False)
   is_active = models.BooleanField(verbose_name=_('Active'), default=False)
   is_superuser = models.BooleanField(verbose_name=_('Is Superuser'), default=False)
   objects = UserManager()

   USERNAME_FIELD = 'email'

   REQUIRED_FIELDS = ['dni']

   def __str__(self) -> str:
      return self.get_username()

   # def parse_fields(self):
   #    for field in self._meta.fields:
   #       if type(field) in (models.fields.CharField, models.fields.EmailField, models.fields.TextField):
   #          setattr(self, field.attname, self.__getattribute__(field.attname).lower())

   # def clean(self) -> None:
   #    self.parse_fields()
   #    return super().clean()

   # def save(self, *args, **kwargs) -> None:
   #    self.clean()
   #    return super().save(*args, **kwargs)

   class Meta:
      verbose_name = _('User')
      verbose_name_plural = _('Users')

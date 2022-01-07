from typing import Optional, TYPE_CHECKING
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext as _
from django.core.validators import MaxLengthValidator


class UserManager(BaseUserManager):

   def _create(self, username: str, email: str, password: Optional[str] = None, **kwargs):
      user: User = self.model(
          _username=username,
          _email=self.normalize_email(email),
          **kwargs,
      )
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_user(self, username: str, email: str, password: Optional[str] = None):
      return self._create(username, email, password)

   def create_superuser(self,
                        username: str,
                        email: str,
                        password: Optional[str] = None,
                        is_superuser: Optional[bool] = True):
      return self._create(username, email, password, is_superuser=is_superuser)


class User(AbstractBaseUser):
   _first_name = models.CharField(verbose_name=_('Name'),
                                  max_length=50,
                                  validators=(MaxLengthValidator(50, 'Máximo permitido 50 carácteres'), ))
   _last_name = models.CharField(verbose_name=_('Last Name'),
                                 max_length=50,
                                 validators=(MaxLengthValidator(50, 'Máximo permitido 50 carácteres'), ))
   _province = models.CharField(verbose_name=_('Provincia'),
                                max_length=50,
                                validators=(MaxLengthValidator(50, 'Máximo permitido 50 carácteres'), ))
   _city = models.CharField(verbose_name=_('City'),
                            max_length=50,
                            validators=(MaxLengthValidator(50, 'Máximo permitido 50 carácteres'), ))
   _email = models.EmailField(verbose_name=_('Email'),
                              max_length=128,
                              unique=True,
                              validators=(MaxLengthValidator(128, 'Máximo permitido 50 carácteres'), ))
   _gender = models.CharField(verbose_name='Gender',
                              max_length=1,
                              choices=(
                                  ('M', _('Male')),
                                  ('F', _('Female')),
                                  ('O', _('Other')),
                              ))
   is_active = models.BooleanField(verbose_name=_('Active'), default=True)
   is_superuser = models.BooleanField(verbose_name=_('Is Superuser'), default=False)
   objects = UserManager()

   USERNAME_FIELD = '_email'
   REQUIRED_FIELDS = ['_username']

   def __str__(self) -> str:
      return self.get_username()

   class Meta:
      verbose_name = _('User')
      verbose_name_plural = _('Users')

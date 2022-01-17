import os
from django.contrib.auth.models import AbstractBaseUser
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy

from apps.authentication.views import activation_token


def get_activation_account_link(instance: AbstractBaseUser):
   path = reverse_lazy('auth:account_activation',
                       kwargs={
                           'uidb64': urlsafe_base64_encode(force_bytes(instance)),
                           'token': activation_token.make_token(instance),
                       })
   return os.getenv('DOMAIN') + path

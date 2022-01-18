import os
from django.contrib.auth.models import AbstractBaseUser
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy

from django.contrib.auth.tokens import PasswordResetTokenGenerator

token_generator = PasswordResetTokenGenerator()


def get_activation_account_link(instance: AbstractBaseUser):
   path = reverse_lazy('auth:account_activation',
                       kwargs={
                           'uidb64': urlsafe_base64_encode(force_bytes(instance)),
                           'token': make_token(instance),
                       })
   return os.getenv('DOMAIN') + path


def make_token(instance: AbstractBaseUser):
   return token_generator.make_token(instance)


def check_token(instance: AbstractBaseUser, token):
   return token_generator.check_token(instance, token)
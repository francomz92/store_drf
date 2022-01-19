import os
from django.contrib.auth.models import AbstractBaseUser
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy
from django.contrib.auth.tokens import PasswordResetTokenGenerator

token_generator = PasswordResetTokenGenerator()


def get_account_activation_link(instance: AbstractBaseUser):
   path = reverse_lazy('auth:account_activation',
                       kwargs={
                           'uidb64': urlsafe_base64_encode(force_bytes(instance.pk)),
                           'token': make_token(instance),
                       })
   return os.getenv('DOMAIN') + path


def get_password_reset_link(reset_password_token):
   path = reverse_lazy('password_reset:reset-password-confirm')
   return os.getenv('DOMAIN') + path + f'?token={reset_password_token.key}'


def make_token(instance: AbstractBaseUser):
   return token_generator.make_token(instance)


def check_token(instance: AbstractBaseUser, token):
   return token_generator.check_token(instance, token)
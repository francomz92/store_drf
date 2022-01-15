import os
from re import template
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.context import Context
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.conf.global_settings import EMAIL_HOST_USER

from rest_framework.reverse import reverse

from .views import activation_token
from apps.users import serializers as user_serializers

DOMAIN = str(os.getenv('DOMAIN'))


@receiver(post_save, sender=get_user_model())
def send_confirmation_email(sender, instance, created, **kwargs):
   if created:
      uid = urlsafe_base64_encode(force_bytes(instance))
      token = activation_token.make_token(instance)
      path = reverse('auth:account_activation', args=(uid, token))
      subject = 'Account confirmation'
      message = get_template('account_activation_message.html').render({
          'user':
          user_serializers.UserSingleSerializer(instance).data,
          'url':
          ''.join((DOMAIN, path, uid, token)),
          'from':
          EMAIL_HOST_USER,
      })
      mail = EmailMessage(subject, message, to=[instance.email], from_email=EMAIL_HOST_USER)
      mail.content_subtype = 'html'
      mail.send()
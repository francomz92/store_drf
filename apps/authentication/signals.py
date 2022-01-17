import os
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.conf.global_settings import EMAIL_HOST_USER

from utils.mail import create_html_mail

from apps.users import serializers as user_serializers
from utils.auth import get_activation_account_link

DOMAIN = str(os.getenv('DOMAIN'))


@receiver(post_save, sender=get_user_model())
def send_confirmation_email(sender, instance, created, **kwargs):
   if created:
      url = get_activation_account_link(instance)
      subject = 'Account confirmation'
      message = get_template('account_activation_message.html').render({
          'user':
          user_serializers.UserSingleSerializer(instance).data,
          'url':
          url,
          'from':
          EMAIL_HOST_USER,
      })
      mail = create_html_mail(subject, message, [instance.email], EMAIL_HOST_USER)
      mail.send(fail_silently=False)
import os
import threading

from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import get_template
from django.conf import settings

from django_rest_passwordreset.signals import reset_password_token_created

from utils.mail import create_html_mail
from utils.auth import get_account_activation_link, get_password_reset_link

from apps.users import serializers as user_serializers


@receiver(post_save, sender=get_user_model())
def send_confirmation_email(sender, instance, created, **kwargs):
   if created:
      subject = 'Account confirmation'
      context = {
          'user': user_serializers.UserSingleSerializer(instance).data,
          'url': get_account_activation_link(instance),
          'from': settings.DEFAULT_FROM_EMAIL,
      }
      email_html_message = get_template('account_activation_message.html').render(context)
      mail = create_html_mail(
          subject,
          email_html_message,
          [instance.email],
          settings.DEFAULT_FROM_EMAIL,
          (settings.DEFAULT_FROM_EMAIL, ),
      )
      thread = threading.Thread(target=mail.send, kwargs={'fail_silently': False})
      thread.start()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
   context = {
       'user': reset_password_token.user,
       'url': get_password_reset_link(reset_password_token),
       'from': settings.DEFAULT_FROM_EMAIL,
   }
   email_html_message = get_template('reset_password.html').render(context)

   mail = create_html_mail(
       f'Password Reset for {reset_password_token.user.email}',
       email_html_message,
       (reset_password_token.user.email, ),
       settings.DEFAULT_FROM_EMAIL,
       (settings.DEFAULT_FROM_EMAIL, ),
   )
   thread = threading.Thread(target=mail.send, kwargs={'fail_silently': False})
   thread.start()

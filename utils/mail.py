from typing import List
from django.core.mail import EmailMessage


def create_html_mail(subject: str, template, to: List[str], from_email: str) -> EmailMessage:
   mail = EmailMessage(subject, template, to=[*to], from_email=from_email)
   mail.content_subtype = 'html'
   return mail

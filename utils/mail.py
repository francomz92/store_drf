from typing import List, Sequence

from django.core.mail import EmailMessage


def create_html_mail(subject: str,
                     template,
                     to: Sequence[str],
                     from_email: str,
                     bcc: Sequence[str] | None = None) -> EmailMessage:
   mail = EmailMessage(subject=subject, body=template, to=to, from_email=from_email, bcc=bcc)
   mail.content_subtype = 'html'
   return mail

from django.contrib.auth import tokens
from django.utils.translation import gettext as _
from rest_framework import response, status, generics, exceptions

from . import serializers


class SignUpView(generics.GenericAPIView):
   serializer_class = serializers.SignUpSerializer

   def post(self, request, *args, **kwargs):
      user_serializer = self.get_serializer(data=request.data)
      if user_serializer.is_valid():
         user_serializer.save(is_active=False)
         return response.Response(
             {
                 'message':
                 _('An email has been sent to your registration please check your email and verifi your account'
                   ),
             },
             status=status.HTTP_201_CREATED,
         )
      raise exceptions.ValidationError(user_serializer.errors)


activation_token = tokens.PasswordResetTokenGenerator()

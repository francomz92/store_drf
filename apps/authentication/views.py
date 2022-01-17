from django.contrib.auth import tokens, get_user_model
from django.utils.translation import gettext as _
from django.utils import http
from rest_framework import response, status, generics, exceptions
from rest_framework_simplejwt import views as jwt_views

from . import serializers


class SignUpView(generics.GenericAPIView):
   serializer_class = serializers.SignUpSerializer

   def post(self, request, *args, **kwargs):
      user_serializer = self.get_serializer(data=request.data)
      if user_serializer.is_valid():
         user_serializer.save()
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


class AuthenticationView(generics.GenericAPIView):

   def get(self, request, *args, **kwargs):
      try:
         uid = http.urlsafe_base64_decode(kwargs['uidb64']).decode()
         user = get_user_model().objects.get(email=uid)
      except Exception as err:
         user = None
      if user is not None and activation_token.check_token(user, kwargs['token']):
         user.is_active = True
         user.save()
         return response.Response(
             {
                 'message': _('Your account has been activated successfully'),
             },
             status=status.HTTP_200_OK,
         )
      raise exceptions.ValidationError({
          'message': _('Activation link is invalid or expired'),
      }, )


class LogInView(jwt_views.TokenObtainPairView):
   serializer_class = serializers.LogInSerializer
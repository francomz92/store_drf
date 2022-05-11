import json
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import http

from rest_framework import response, status, generics, exceptions

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken

from utils.auth import check_token

from . import serializers


class SignUpView(generics.GenericAPIView):
   serializer_class = serializers.SignUpSerializer

   def post(self, request, *args, **kwargs):
      user_serializer = self.get_serializer(data=request.data)
      user_serializer.is_valid(raise_exception=True)
      user_serializer.save()
      return response.Response(
          {
              'message':
              _('An email has been sent to your registration please check your email and verifi your account'
                ),
          },
          status=status.HTTP_201_CREATED,
      )


class AuthenticationView(generics.GenericAPIView):

   def get(self, request, *args, **kwargs):
      try:
         uid = http.urlsafe_base64_decode(kwargs['uidb64']).decode()
         user = get_user_model().objects.get(pk=uid)
      except Exception as err:
         user = None
      if user is not None and check_token(user, kwargs['token']):
         setattr(user, 'is_active', True)
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


class LogOutView(generics.GenericAPIView):

   serializer_class = serializers.LogInSerializer

   def post(self, request, *args, **kwargs):
      data = json.loads(request.body)
      user = get_user_model().objects.filter(id=data['user']['id']).first()
      token = OutstandingToken.objects.filter(user=user).order_by('-created_at').first()
      if user.is_authenticated and data['refresh'] == token.token:
         RefreshToken.for_user(user=user)
         return response.Response(
             {
                 'message': _('You have been logged out successfully'),
             },
             status=status.HTTP_200_OK,
         )
      raise exceptions.NotAuthenticated('You are not authenticated')


class PasswordChangeView(generics.UpdateAPIView):

   serializer_class = serializers.PasswordChangeSerializer

   def get_object(self):
      return self.request.user

   def update(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance=instance, data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_update(serializer)
      data = {**serializer.data, 'message': _('Your password has been changed successfully')}
      return response.Response(data=data, status=status.HTTP_200_OK)

   # def perform_update(self, serializer):
   #    serializer.save()
   #    serializer.data.setdefault('message', _('Your password has been changed successfully'))
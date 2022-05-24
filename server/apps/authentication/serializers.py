from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from rest_framework import serializers, exceptions

from rest_framework_simplejwt import serializers as jwt_serializers

from apps.users import serializers as user_serializers


class SignUpSerializer(serializers.ModelSerializer):

   password_confirmation = serializers.CharField(max_length=128, required=True)

   class Meta:
      model = get_user_model()
      exclude = (
          'id',
          'is_superuser',
          'is_staff',
          'is_active',
          'last_login',
          'groups',
          'user_permissions',
      )
      extra_kwargs = {
          'password': {
              'write_only': True,
          },
          'password_confirmation': {
              'write_only': True,
          },
      }

   def validate(self, attrs):
      if attrs.get('password') != attrs.get('password_confirmation'):
         raise exceptions.ValidationError(_('Passwords do not match'))
      return super().validate(attrs)

   def create(self, validated_data):
      validated_data.pop('password_confirmation')
      return super().create(validated_data)


class LogInSerializer(jwt_serializers.TokenObtainPairSerializer):

   def validate(self, attrs):
      data = super().validate(attrs)
      data.setdefault('user', user_serializers.UserSingleSerializer(self.user).data)
      data.setdefault('message', _(f'Welcome back, {getattr(self.user, "first_name")}'))
      return data


class PasswordChangeSerializer(serializers.Serializer):

   old_password = serializers.CharField(max_length=128, required=True, write_only=True)
   new_password = serializers.CharField(max_length=128, required=True, write_only=True)
   confirm_password = serializers.CharField(max_length=128, required=True, write_only=True)

   class Meta:
      fields = ('old_password', 'new_password', 'confirm_password')

   def validate(self, attrs):
      user = getattr(self.context.get('request'), 'user')
      if not user.check_password(attrs.get('old_password')):
         raise exceptions.ValidationError(_('Old password is not correct'))
      if attrs.get('new_password') != attrs.get('confirm_password'):
         raise exceptions.ValidationError(_('Passwords do not match'))
      if attrs.get('new_password') == attrs.get('old_password'):
         raise exceptions.ValidationError(_('New password is the same as old password'))
      return attrs

   def update(self, instance, validated_data):
      instance.set_password(validated_data.get('new_password'))
      instance.save()
      return instance
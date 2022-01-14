from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers, exceptions


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



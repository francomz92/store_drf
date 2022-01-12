from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import crypto


class UsersListSerializer(serializers.ModelSerializer):

   class Meta:
      model = get_user_model()
      exclude = (
          'is_superuser',
          'groups',
          'user_permissions',
          'password',
      )
      read_only_fields = (
          'id',
          'is_staff',
          'is_active',
          'last_login',
      )

   def create(self, validated_data):
      validated_data['password'] = crypto.get_random_string(length=10,
                                                            allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                                            'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                                            '23456789')
      return super().create(validated_data)


class UserSingleSerializer(serializers.ModelSerializer):

   class Meta:
      model = get_user_model()
      exclude = (
          'password',
          'is_superuser',
          'groups',
          'user_permissions',
      )
      read_only_fields = (
          'id',
          'email',
          'last_login',
          'is_staff',
      )

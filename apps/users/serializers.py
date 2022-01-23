from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions


class UsersListSerializer(serializers.ModelSerializer):

   class Meta:
      model = get_user_model()
      exclude = (
          'is_superuser',
          'groups',
          'user_permissions',
          'password',
      )
      read_only_fields = ('id', 'is_staff', 'is_active', 'last_login', 'created_at', 'updated_at')

   def validate_dni(self, value: str):
      if (not value.isnumeric()) or len(value) != 8:
         raise exceptions.ValidationError(detail=f'{value} no es un número de dni válido')
      return value

   def create(self, validated_data):
      validated_data['password'] = validated_data['dni']
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
      read_only_fields = ('id', 'email', 'last_login', 'is_staff', 'dni', 'created_at', 'updated_at')

from rest_framework import serializers
from django.contrib.auth import get_user_model


class UsersListSerializer(serializers.ModelSerializer):

   class Meta:
      model = get_user_model()
      exclude = [
          'is_active',
          'is_superuser',
          'is_staff',
          'groups',
          'user_permissions',
      ]
      extra_kwargs = {
          'password': {
              'write_only': True
          },
      }

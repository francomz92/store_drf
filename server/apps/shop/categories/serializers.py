from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

   class Meta:
      model = models.Category
      fields = serializers.ALL_FIELDS
      read_only_fields = ('id', 'created_at', 'updated_at')

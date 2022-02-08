from rest_framework import serializers

from apps.shop.categories import models as category_models, serializers as category_serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
   category = category_serializers.CategorySerializer()

   class Meta:
      model = models.Product
      fields = '__all__'

   def to_representation(self, instance):
      data = super().to_representation(instance)
      data['category'] = instance.category.name
      if not instance.image_url:
         data['image_url'] = ''
      return data

from rest_framework import serializers, exceptions

from apps.shop.products import (
    serializers as product_serializers,
    models as product_models,
)
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
   """
       Serializer for CartItem model.
   """

   product = product_serializers.ProductSerializer(read_only=True)

   class Meta:
      model = CartItem
      exclude = ('cart', )
      read_only_fields = ('id', 'price')

   def create(self, validated_data):
      product = product_models.Product.objects.get(id=self.context['request'].data['product']['id'])
      validated_data['product'] = product
      if product.active and product.stok > 0 and validated_data['ammount'] <= product.stok:
         return super().create(validated_data)
      raise exceptions.ValidationError({'detail': 'Product is not available'})

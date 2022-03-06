from rest_framework import serializers, exceptions

from apps.shop.products import (
    serializers as product_serializers,
    models as product_models,
)
from utils.carts import is_the_product_avaiable

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
      if is_the_product_avaiable(product, validated_data['ammount']):
         validated_data['product'] = product
         return super().create(validated_data)

   def update(self, instance, validated_data):
      if is_the_product_avaiable(instance.product, validated_data['ammount']):
         return super().update(instance, validated_data)

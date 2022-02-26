from rest_framework import serializers

from apps.shop.products import serializers as product_serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
   """
       Serializer for CartItem model.
   """

   product = product_serializers.ProductSerializer()

   class Meta:
      model = CartItem
      fields = serializers.ALL_FIELDS

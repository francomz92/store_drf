from typing import List
from rest_framework import serializers

from .models import Order, OrderItem
from apps.shop.cart import serializers as cart_serializers


class OrderItemsSerializer(serializers.ModelSerializer):

   class Meta:
      model = OrderItem
      exclude = ('order', )
      read_only_fields = ('id', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):

   items = serializers.ListSerializer(child=OrderItemsSerializer())

   class Meta:
      model = Order
      fields = ('id', 'created_at', 'updated_at', 'items', 'total')
      read_only_fields = ('id', 'created_at', 'updated_at')

   def create(self, validated_data):
      items = validated_data.pop('items')
      order = Order.objects.create(**validated_data)
      for item in items:
         OrderItem.objects.create(**item, order=order)
      return order

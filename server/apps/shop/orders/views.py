from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from .models import Order
from .serializers import OrderSerializer
from .permissions import OwnCartItemsPermissions


class OrderListView(generics.ListCreateAPIView):
   model = Order
   serializer_class = OrderSerializer
   permission_classes = (permissions.IsAuthenticated, OwnCartItemsPermissions)

   def get_queryset(self):
      return self.model.objects.filter(user=self.kwargs['user_id'])

   def perform_create(self, serializer):
      user = get_object_or_404(get_user_model(), id=self.kwargs['user_id'])
      serializer.save(user=user)

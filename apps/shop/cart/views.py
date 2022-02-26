from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from .serializers import CartItemSerializer, CartItem
from .permissions import OwnCartItemsPermissions


class PrivateCartItemsListView(generics.ListAPIView):
   model = CartItem
   serializer_class = CartItemSerializer
   permission_classes = (
       permissions.IsAuthenticated,
       OwnCartItemsPermissions,
   )

   def get_queryset(self):
      user = get_object_or_404(get_user_model(), id=self.kwargs['user_id'])
      return CartItem.objects.filter(cart=getattr(user, 'user_cart'))

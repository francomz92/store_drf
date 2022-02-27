from rest_framework import generics, permissions

from utils.users import get_current_user
from .serializers import CartItemSerializer, CartItem
from .permissions import OwnCartItemsPermissions


class PrivateCartItemsListView(generics.ListCreateAPIView):
   model = CartItem
   serializer_class = CartItemSerializer
   permission_classes = (
       permissions.IsAuthenticated,
       OwnCartItemsPermissions,
   )

   def get_queryset(self):
      user = get_current_user(id=self.kwargs['user_id'])
      return CartItem.objects.filter(cart=getattr(user, 'user_cart'))

   def perform_create(self, serializer):
      user = get_current_user(id=self.kwargs['user_id'])
      serializer.save(cart=getattr(user, 'user_cart'))
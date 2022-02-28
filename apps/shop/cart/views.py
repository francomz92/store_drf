from rest_framework import generics, permissions, mixins, response, status, exceptions

from utils.users import get_current_user
from .serializers import CartItemSerializer, CartItem
from .permissions import OwnCartItemsPermissions


class PrivateListCartItemsView(generics.ListCreateAPIView):
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


class PrivateUpdateCartItemView(mixins.UpdateModelMixin, generics.GenericAPIView):
   model = CartItem
   serializer_class = CartItemSerializer
   permission_classes = (
       permissions.IsAuthenticated,
       OwnCartItemsPermissions,
   )

   def get_object(self):
      user = get_current_user(id=self.kwargs['user_id'])
      return CartItem.objects.filter(id=self.kwargs['item_id'], cart=getattr(user, 'user_cart')).first()

   def put(self, request, *args, **kwargs):
      serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return response.Response(serializer.data, status=status.HTTP_200_OK)
      raise exceptions.ValidationError(serializer.errors)

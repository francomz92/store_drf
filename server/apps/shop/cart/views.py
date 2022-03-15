from django.db.models import Prefetch
from django.shortcuts import get_object_or_404

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
      return self.model.objects.prefetch_related(Prefetch('cart'), Prefetch('product')) \
         .filter(cart=getattr(user, 'user_cart'))

   def get(self, request, *args, **kwargs):
      page = self.paginate_queryset(self.get_queryset())
      if page is not None:
         serializer = self.get_serializer(page, many=True)
         data = {
             'items': serializer.data,
             'total_price': self.model.get_total_price(serializer.data)[0],
             'total_without_discount': self.model.get_total_price(serializer.data)[1],
         }
         return self.get_paginated_response(data)

      serializer = self.get_serializer(self.get_queryset(), many=True)
      data = {
          'items': serializer.data,
          'total_price': self.model.get_total_price(serializer.data)[0],
          'total_without_discount': self.model.get_total_price(serializer.data)[1],
      }
      return response.Response(data=data, status=status.HTTP_200_OK)

   def post(self, request, *args, **kwargs):
      data, existent_item = self._clean_request_data(request)
      if data:
         return super().create(request, *args, **kwargs)
      return response.Response(self.get_serializer(existent_item).data, status=status.HTTP_200_OK)

   def perform_create(self, serializer):
      user = get_current_user(id=self.kwargs['user_id'])
      serializer.save(cart=getattr(user, 'user_cart'))

   def _clean_request_data(self, request):
      ''' Increase item amount if exists in cart '''
      data = request.data.copy()
      existent_item = self.get_queryset().filter(product__id=data['product']['id']).first()
      if existent_item is not None and int(data['product']['id']) == existent_item.product.id:
         existent_item.amount += 1
         existent_item.save()
         data = None
      return data, existent_item


class PrivateUpdateCartItemView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
   model = CartItem
   serializer_class = CartItemSerializer
   permission_classes = (
       permissions.IsAuthenticated,
       OwnCartItemsPermissions,
   )

   def get_object(self) -> CartItem | None:
      user = get_current_user(id=self.kwargs['user_id'])
      return get_object_or_404(self.model, id=self.kwargs['item_id'], cart=getattr(user, 'user_cart'))

   def put(self, request, *args, **kwargs):
      data = self._clean_request_data(request)
      if data:
         serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
         if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
         raise exceptions.ValidationError(serializer.errors)
      return response.Response({'message': 'Item deleted.'}, status=status.HTTP_200_OK)

   def delete(self, request, *args, **kwargs):
      item = self.get_object()
      if item:
         item.delete()
         return response.Response(status=status.HTTP_204_NO_CONTENT)
      raise exceptions.NotFound(detail='Item not found.')

   def _clean_request_data(self, request):
      ''' Delete item if their amount is less than or equal to 0 '''
      if int(request.data['amount']) < 1:
         self.delete(request)
         return None
      return True
from django.contrib.auth import get_user_model

from rest_framework import permissions, exceptions


class OwnCartItemsPermissions(permissions.BasePermission):
   """ Custom permission class for Cart app. """

   def has_permission(self, request, view):
      request_user_id = request.parser_context['kwargs']['user_id']
      current_user_id = view.request.user.id
      if request_user_id != current_user_id:
         raise exceptions.PermissionDenied()
      return request_user_id == current_user_id

   # def has_object_permission(self, request, view, obj):
   #    user = get_user_model().objects.filter(id=request['user_id']).first()
   #    print(obj.cart.id == getattr(user, 'user_cart').id if user else False)
   #    if request.method in permissions.SAFE_METHODS:
   #       return True
   #    return obj.cart.id == getattr(user, 'user_cart').id if user else False

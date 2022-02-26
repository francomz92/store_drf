from django.contrib.auth import get_user_model

from rest_framework import permissions


class OwnCartItemsPermissions(permissions.BasePermission):
   """ Custom permission class for Cart app. """

   def has_object_permission(self, request, view, obj):
      """ Return `True` if permission is granted, `False` otherwise. """
      if request.method in permissions.SAFE_METHODS:
         return True
      user = get_user_model().objects.filter(id=request['user_id']).first()
      return obj.cart.id == getattr(user, 'user_cart').id if user else False
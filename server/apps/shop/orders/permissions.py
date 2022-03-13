from rest_framework import permissions


class OwnCartItemsPermissions(permissions.BasePermission):
   """ Custom permission class for Cart app. """

   def has_permission(self, request, view):
      request_user_id = request.parser_context['kwargs']['user_id']
      current_user_id = view.request.user.id
      return request_user_id == current_user_id
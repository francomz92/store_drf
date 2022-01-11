from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .filters import UsersFilters

from . import serializers


class UsersListCreateView(ListCreateAPIView):
   serializer_class = serializers.UsersListSerializer
   model = serializer_class.Meta.model
   permission_classes = (permissions.IsAdminUser, )
   filterset_class = UsersFilters

   def get_queryset(self):
      return self.model.objects.all().order_by('-id')


class UserRetrieveUpdateDeactiveView(RetrieveUpdateDestroyAPIView):
   serializer_class = serializers.UserSingleSerializer
   model = serializer_class.Meta.model
   permission_classes = (permissions.IsAdminUser, )
   lookup_field = 'id'
   lookup_url_kwarg = 'id'

   def get_object(self):
      return get_object_or_404(self.model, id=self.kwargs['id'])

   def perform_destroy(self, instance):
      setattr(instance, 'is_active', False)
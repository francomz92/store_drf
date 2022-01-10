from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from django_filters.rest_framework import filters, DjangoFilterBackend

from .filters import UsersFilters

from . import serializers


class UsersListCreateView(ListCreateAPIView):
   serializer_class = serializers.UsersListSerializer
   model = serializer_class.Meta.model
   queryset = model.objects.all().order_by('-id')

   permission_classes = (permissions.IsAdminUser, )

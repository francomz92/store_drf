from django.shortcuts import get_object_or_404

from rest_framework import permissions, generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from . import serializers, filters as users_filters


class UsersListCreateView(generics.ListCreateAPIView):
   serializer_class = serializers.UsersListSerializer
   model = serializers.get_user_model()
   permission_classes = (permissions.IsAuthenticated, )
   filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   filterset_class = users_filters.UsersFilters
   search_fields = ('email', 'first_name', 'last_name')

   def get_queryset(self):
      return self.model.objects.all().order_by('-id')


class UserRetrieveUpdateDeactiveView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = serializers.UserSingleSerializer
   model = serializers.get_user_model()
   permission_classes = (permissions.IsAdminUser, )
   lookup_field = 'id'
   lookup_url_kwarg = 'id'

   def get_object(self):
      return get_object_or_404(self.model, id=self.kwargs['id'])

   def perform_destroy(self, instance):
      setattr(instance, 'is_active', False)

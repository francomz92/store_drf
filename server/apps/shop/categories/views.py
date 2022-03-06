from django.shortcuts import get_object_or_404

from rest_framework import generics, filters, permissions

from . import serializers


class CategoryListCreateView(generics.ListCreateAPIView):
   serializer_class = serializers.CategorySerializer
   filter_backends = (filters.SearchFilter, )
   search_fields = ('name', )
   permission_classes = (permissions.IsAuthenticated, )

   def get_queryset(self):
      return serializers.models.Category.objects.all().order_by('id')


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = serializers.CategorySerializer
   permission_classes = (permissions.IsAuthenticated, )

   def get_object(self):
      return get_object_or_404(serializers.models.Category, id=self.kwargs['id'])

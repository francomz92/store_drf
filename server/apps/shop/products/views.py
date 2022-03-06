from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, permissions, parsers

from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers, pagination, filters as products_filters


class PublicProductListView(generics.ListAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   filterset_class = products_filters.ProductFilter
   search_fields = ('name', )
   pagination_class = pagination.ProductPagination

   def get_queryset(self):
      return self.model.objects.select_related('category').filter(active=True)


class PublicRetrieveProductView(generics.RetrieveAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   lookup_field = 'id'

   def get_object(self):
      return get_object_or_404(klass=self.model, id=self.kwargs['id'], active=True)


class PrivateProductListCreateView(generics.ListCreateAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   filterset_class = products_filters.ProductFilter
   search_fields = ('name', )
   permission_classes = (permissions.IsAuthenticated, )
   pagination_class = pagination.ProductPagination
   parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser)

   def get_queryset(self):
      return self.model.objects.select_related('category').all()


class PrivateProductRetrieveUpdateDeactivateView(generics.RetrieveUpdateDestroyAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   lookup_field = 'id'
   permission_classes = (permissions.IsAuthenticated, )

   def get_object(self):
      return get_object_or_404(klass=self.model, id=self.kwargs['id'])

   def perform_destroy(self, instance):
      setattr(instance, 'active', False)
      instance.save()


class PrivateProductDestroyView(generics.DestroyAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   lookup_field = 'id'
   permission_classes = (permissions.IsAuthenticated, )

   def get_object(self):
      return get_object_or_404(klass=self.model, id=self.kwargs['id'])
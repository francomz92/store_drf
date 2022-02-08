from rest_framework import generics, filters, permissions

from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers, pagination, permissions as products_prermissions, filters as products_filters


class PublicProductListView(generics.ListAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   filterset_class = products_filters.ProductFilter
   search_fields = ('name', )
   pagination_class = pagination.ProductPagination

   def get_queryset(self):
      return self.model.objects.filter(active=True)


class PrivateProductListView(generics.ListAPIView):
   model = models.Product
   serializer_class = serializers.ProductSerializer
   filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   filterset_class = products_filters.ProductFilter
   search_fields = ('name', )
   permission_classes = (permissions.IsAuthenticated, )
   pagination_class = pagination.ProductPagination

   def get_queryset(self):
      return self.model.objects.filter()
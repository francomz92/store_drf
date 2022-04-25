from django.urls import path

from apps.shop.products.views import (
    PrivateProductListCreateView,
    PrivateProductRetrieveUpdateDeactivateView,
    PrivateProductDestroyView,
    PublicProductListView,
    PublicRetrieveProductView,
)

app_name = 'products'

urlpatterns = [
    # Public Endpoints
    path('public/products/', PublicProductListView.as_view(), name='public_products'),
    path('public/products/<int:id>/', PublicRetrieveProductView.as_view(), name='public_product_detail'),

    # Private Endpoints
    path('private/products/', PrivateProductListCreateView.as_view(), name='private_products'),
    path('private/products/<int:id>/',
         PrivateProductRetrieveUpdateDeactivateView.as_view(),
         name='private_product_detail'),
    path('private/products/<int:id>/delete/',
         PrivateProductDestroyView.as_view(),
         name='private_product_delete'),
]
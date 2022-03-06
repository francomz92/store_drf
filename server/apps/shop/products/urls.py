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
    path('products/public/', PublicProductListView.as_view(), name='public_products'),
    path('products/public/<int:id>/', PublicRetrieveProductView.as_view(), name='public_product_detail'),

    # Private Endpoints
    path('products/private/', PrivateProductListCreateView.as_view(), name='private_products'),
    path('products/private/<int:id>/',
         PrivateProductRetrieveUpdateDeactivateView.as_view(),
         name='private_product_detail'),
    path('products/private/<int:id>/delete/',
         PrivateProductDestroyView.as_view(),
         name='private_product_delete'),
]
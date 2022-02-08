from django.urls import path

from apps.shop.products.views import PrivateProductListView, PublicProductListView, PublicRetrieveProductView

app_name = 'products'

urlpatterns = [
    # Public Endpoints
    path('products/public/', PublicProductListView.as_view(), name='public_products'),
    path('products/public/<int:id>/', PublicRetrieveProductView.as_view(), name='public_product_detail'),

    # Private Endpoints
    path('products/private/', PrivateProductListView.as_view(), name='private_products'),
]
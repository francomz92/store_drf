from django.urls import path

from apps.shop.products.views import PrivateProductListView, PublicProductListView

app_name = 'products'

urlpatterns = [
    path('products/public/', PublicProductListView.as_view(), name='public_products'),
    path('products/private/', PrivateProductListView.as_view(), name='private_products'),
]
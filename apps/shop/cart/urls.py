from django.urls import path

from .views import PrivateCartItemsListView

app_name = 'cart'

urlpatterns = [
    path('cart/<int:user_id>/cart_items/', PrivateCartItemsListView.as_view(), name='private_cart_items'),
]
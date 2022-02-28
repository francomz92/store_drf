from django.urls import path

from .views import PrivateListCartItemsView, PrivateUpdateCartItemView

app_name = 'cart'

urlpatterns = [
    path('cart/<int:user_id>/cart_items/', PrivateListCartItemsView.as_view(), name='private_cart_items'),
    path('cart/<int:user_id>/cart_items/<int:item_id>/',
         PrivateUpdateCartItemView.as_view(),
         name='private_cart_item_detail'),
]
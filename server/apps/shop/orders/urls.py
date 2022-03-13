from django.urls import path

from .views import OrderListView

app_name = 'orders'

urlpatterns = [
    path('<int:user_id>/orders/', OrderListView.as_view(), name='private_orders'),
]
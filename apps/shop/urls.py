from django.urls import path, include

app_name = 'shop'

urlpatterns = [
    path('shop/', include('apps.shop.categories.urls')),
    path('shop/', include('apps.shop.products.urls')),
]

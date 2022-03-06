from django.urls import path

from apps.shop.categories.views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView

app_name = 'categories'

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='categories'),
    path('category/<int:id>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category_detail'),
]
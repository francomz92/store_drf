from django.urls import path

from apps.shop.categories.views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, PublicCategoryListView

app_name = 'categories'

urlpatterns = [
    # Private Endpoints
    path('private/category/', CategoryListCreateView.as_view(), name='categories'),
    path('private/category/<int:id>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category_detail'),
    # Public Endpoints
    path('public/category/', PublicCategoryListView.as_view(), name='category_list'),
]
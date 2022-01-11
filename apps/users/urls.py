from django.urls import path
from .views import UsersListCreateView, UserRetrieveUpdateDeactiveView

app_name = 'users'

urlpatterns = [
    path('users/', UsersListCreateView.as_view(), name='users_list_create'),
    path('users/<int:id>/', UserRetrieveUpdateDeactiveView.as_view(), name='single_user'),
]

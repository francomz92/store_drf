from django.urls import path
from .views import UsersListCreateView

app_name = 'users'

urlpatterns = [
    path('users/', UsersListCreateView.as_view(), name='users_list_create'),
]

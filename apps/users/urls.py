from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDeactiveView

app_name = 'users'

urlpatterns = [
    path('users/', UsersListCreateView.as_view(), name='users'),
    path('users/<int:id>/', UserRetrieveUpdateDeactiveView.as_view(), name='user_detail'),
]

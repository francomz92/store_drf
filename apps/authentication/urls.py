from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import LogOutView, SignUpView, AuthenticationView, LogInView

app_name = 'auth'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activation/<uidb64>/<token>/', AuthenticationView.as_view(), name='account_activation'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

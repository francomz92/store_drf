from rest_framework.urls import path
from .views import SignUpView, AuthenticationView

app_name = 'auth'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activation/<uidb64>/<token>/', AuthenticationView.as_view(), name='account_activation'),
]

from rest_framework.urls import path
from .views import SignUpView

app_name = 'auth'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

from typing import List

from django.urls import URLPattern, URLResolver, path, include, re_path
from django.contrib import admin

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Project Urls
project_urls: List[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.authentication.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.shop.urls')),
]

# Doc Settings
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

doc_urls: List[URLPattern | URLResolver] = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# UrlPatterns
urlpatterns = project_urls + doc_urls

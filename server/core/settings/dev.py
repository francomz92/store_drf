from datetime import timedelta

from corsheaders.defaults import default_headers, default_methods

from .base import *

SECRET_KEY = os.getenv('DRF_SECRET_KEY')

DEBUG = True

# Hosts Settings
ALLOWED_HOSTS = ['*']

# Datebases Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Django Rest Framework Settings
REST_FRAMEWORK = {
    #  'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser', ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny', ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication', ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend', ),
}

# CORS_ALLOW_ALL_ORIGIN = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://*',
    'https://*',
    'http://localhost:8080',
]
# CORS_ALLOWED_ORIGIN_REGEXES: List[str] = ['http://*', 'https://*']  # Para permitir patrones de url
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False
CORS_PREFLIGHT_MAX_AGE = 3600
CORS_ALLOW_METHODS = list(default_methods)
CORS_ALLOW_HEADERS = list(default_headers) + ['HTTP_AUTHORIZATION']

# Simple JWR Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=5),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': os.getenv('ENCRYPTION_TYPE'),
    'SIGNING_KEY': os.getenv('DRF_SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('test', ),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(seconds=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(minutes=1),
}

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT').__str__())
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# Media Storage Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = 1
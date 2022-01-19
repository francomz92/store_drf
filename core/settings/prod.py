from typing import Dict, List, Optional
from datetime import timedelta

from .base import *

SECRET_KEY: Optional[str] = os.getenv('DRF_SECRET_KEY')

DEBUG: bool = False

ALLOWED_HOSTS: List[Optional[str]] = [os.getenv('DOMAIN')]

DATABASES: Dict[str, Dict[str, Optional[str]]] = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication', ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

CORS_ALLOWED_ORIGINS: List[str] = []
CORS_ALLOWED_ORIGIN_REGEXES: List[str] = []  # Para permitir patrones de url
CORS_ALLOW_ALL_ORIGINS: bool = False
CORS_ALLOW_CREDENTIALS: bool = False

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(str(os.getenv('TOKEN_LIFETIME')))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(str(os.getenv('TOKEN_REFRESH_LIFETIME')))),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': os.getenv('ENCRYPTION_TYPE'),
    'SIGNING_KEY': os.getenv('DRF_SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer', ),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=int(str(os.getenv('TOKEN_LIFETIME')))),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=int(str(os.getenv('TOKEN_REFRESH_LIFETIME')))),
}
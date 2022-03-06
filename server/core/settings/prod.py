from datetime import timedelta

from corsheaders.defaults import default_headers, default_methods

from .base import *

SECRET_KEY = os.getenv('DRF_SECRET_KEY')

DEBUG = False

# Hosts Settings
ALLOWED_HOSTS = [
    os.getenv('DOMAIN').__str__(),
]

# Datebases Settings
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE').__str__(),
        'NAME': os.getenv('DB_NAME').__str__(),
        'USER': os.getenv('DB_USER').__str__(),
        'PASSWORD': os.getenv('DB_PASSWORD').__str__(),
        'HOST': os.getenv('DB_HOST').__str__(),
        'PORT': os.getenv('DB_PORT').__str__(),
    }
}

# Django Rest Framework Settings
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

# Cors Settings
CORS_ALLOWED_ORIGINS = []
CORS_ALLOWED_ORIGIN_REGEXES = []  # Para permitir patrones de url
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_METHODS = list(default_methods)
CORS_ALLOW_HEADERS = list(default_headers) + ['HTTP_AUTHORIZATION']

# Simple JWR Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('TOKEN_LIFETIME').__str__())),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.getenv('TOKEN_REFRESH_LIFETIME').__str__())),
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
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('TOKEN_LIFETIME').__str__())),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=int(os.getenv('TOKEN_REFRESH_LIFETIME').__str__())),
}

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT').__str__())
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# S3 Storage Settings
AWS_ACCESS_KEY_ID = os.getenv('S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('S3_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('S3_REGION_NAME')
AWS_S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
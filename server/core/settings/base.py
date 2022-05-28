import os
from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers, default_methods

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True if os.getenv('ENV', 'dev') == 'dev' else False

SECRET_KEY = os.getenv('DRF_SECRET_KEY', 'django-insecure-=)%d-sqe9k=mg8c5*d%z1b^ve*e4_xb=0n0be^ry8_!rlr%#r)')

ALLOWED_HOSTS = ['*' if DEBUG else os.getenv('ALLOWED_HOSTS', '*')]

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.authentication.apps.AuthenticationConfig',
    'apps.shop.categories.apps.CategoriesConfig',
    'apps.shop.products.apps.ProductsConfig',
    'apps.shop.cart.apps.CartConfig',
    'apps.shop.orders.apps.OrdersConfig',
]

THIRD_APPS = [
    'rest_framework',
    'drf_yasg',
    #  'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_rest_passwordreset',
    'corsheaders',
    'django_filters',
    'admin_reorder',
]

INSTALLED_APPS = [*BASE_APPS, *LOCAL_APPS, *THIRD_APPS]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'auth:login'
LOGOUT_URL = 'auth:logout'

AUTH_USER_MODEL = 'users.User'

# Django Rest Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser', ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny', ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication', ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend', ),
}

# Cors Settings
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False
CORS_PREFLIGHT_MAX_AGE = 3600
CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADERS = (*default_headers, 'HTTP_AUTHORIZATION')

# JWT Settings
SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': os.getenv('ENCRYPTION_TYPE', 'HS256'),
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(hours=int(os.getenv('TOKEN_LIFETIME', '24'))),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(hours=int(os.getenv('TOKEN_REFRESH_LIFETIME', '24'))),
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=int(os.getenv('TOKEN_LIFETIME', '24'))),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=int(os.getenv('TOKEN_REFRESH_LIFETIME', '24'))),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}

# Admin Site Ordering
ADMIN_REORDER = (
    {
        'app': 'auth',
        'label': 'Users',
        'models': (
            'users.User',
            'auth.Group',
        )
    },
    {
        'app':
        'token_blacklist',
        'label':
        'Tokens',
        'models': (
            'token_blacklist.BlacklistedToken',
            'token_blacklist.OutstandingToken',
            'django_rest_passwordreset.ResetPasswordToken',
        )
    },
    {
        'app':
        'categories',
        'label':
        'Shop',
        'models': (
            'categories.Category',
            'products.Product',
            'cart.Cart',
            'cart.CartItem',
            'orders.Order',
            'orders.OrderItem',
        )
    },
)
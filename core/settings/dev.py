from typing import Dict, List
from .base import *
from .drf import *
from .cors import *
from .simple_jwt import *

SECRET_KEY: str = 'django-insecure-=)%d-sqe9k=mg8c5*d%z1b^ve*e4_xb=0n0be^ry8_!rlr%#r)'

DEBUG: bool = True

ALLOWED_HOSTS: List[str] = ['*']

DATABASES: Dict[str, Dict] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS: List[str] = ['http://localhost:8000']

SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(seconds=30)
SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'] = timedelta(minutes=1)
SIMPLE_JWT['AUTH_HEADER_TYPES'] = ('test', )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
from typing import Dict, List, Optional
from .base import *
from .drf import *
from .cors import *
from .simple_jwt import *

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

CORS_ALLOWED_ORIGINS: List[str] = []

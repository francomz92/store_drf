import os
from django.core.asgi import get_asgi_application
from env_tools import ENVIROMENT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{ENVIROMENT}')

application = get_asgi_application()

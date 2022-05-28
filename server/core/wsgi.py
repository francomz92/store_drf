import os
from env_tools import ENVIROMENT

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{ENVIROMENT}')

application = get_wsgi_application()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{os.getenv("ENV", "dev")[:3].lower()}')

application = get_wsgi_application()

import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

load_dotenv('.env')


def get_enviroment():
   """ Returns the current enviroment. """
   ENV = os.getenv('ENV', 'dev')
   if ENV == "dev": return "dev"
   elif ENV == "prod": return "prod"
   raise ValueError(_('''Invalid ENV value
         \nENV must be "dev" or "prod"
   '''))


ENVIROMENT = get_enviroment()
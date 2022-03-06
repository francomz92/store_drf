from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


def get_current_user(id: int):
   return get_object_or_404(get_user_model(), id=id)
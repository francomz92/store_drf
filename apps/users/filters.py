from django.contrib.auth import get_user_model

from django_filters.rest_framework import filterset


class UsersFilters(filterset.FilterSet):

   class Meta:
      model = get_user_model()
      fields = {
          'email': ('exact', ),
          'province': ('exact', ),
          'city': ('exact', ),
          'zip_code': ('exact', ),
      }

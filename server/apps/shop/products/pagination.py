from collections import OrderedDict

from rest_framework import pagination, response

from . import models


class ProductPagination(pagination.PageNumberPagination):
   page_size = 20
   page_size_query_param = 'page_size'
   max_page_size = 100

   # def get_paginated_response(self, data):
   #    return response.Response(
   #        OrderedDict([
   #            ('count', self.page.paginator.count),
   #            ('next', self.get_next_link()),
   #            ('previous', self.get_previous_link()),
   #            ('data', data),
   #        ]))

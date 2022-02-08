from django.urls import reverse_lazy

from apps.shop.categories import models

Category = models.Category


def create_category(name: str) -> Category:
   return Category.objects.create(name=name)


def get_category_detail_url(id: int) -> str:
   return reverse_lazy('shop:categories:category_detail', kwargs={'id': id})
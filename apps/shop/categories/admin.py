from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id', 'name')
   list_display_links = ('name', )
   search_fields = ('name', )
   search_help_text = 'Search by Name'
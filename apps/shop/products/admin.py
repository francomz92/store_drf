from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'category', 'unit_price', 'stok', 'offer', 'created_at', 'updated_at')
   list_display_links = ('id', 'name')
   search_fields = ('category', 'name')
   list_filter = ('category', )
   search_help_text = 'Search by Category or Name'
   autocomplete_fields = ('category', )
   list_filter = ('category', )
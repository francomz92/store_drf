from csv import list_dialects
from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
   list_display = ('id', 'user', 'total', 'updated_at')
   search_fields = ('user', )
   autocomplete_fields = ('user', )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
   list_display = ('id', 'cart', 'product', 'ammount', 'price', 'updated_at')
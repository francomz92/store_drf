from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ('id', 'user', 'created_at', 'updated_at')
   list_filter = ('created_at', )
   search_fields = ('user', )
   autocomplete_fields = ('user', )


@admin.register(OrderItem)
class OrderItemsAdmin(admin.ModelAdmin):
   list_display = ('id', 'order', 'product', 'ammount', 'price', 'updated_at')
   search_fields = ('order', )
   autocomplete_fields = ('order', )
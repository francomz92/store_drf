from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
   list_display = ('id', 'email', 'first_name', 'is_superuser', 'is_staff', 'is_active')
   list_display_links = ('email', )

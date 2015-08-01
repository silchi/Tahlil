from django.contrib import admin

from .models import Cart

class CartUserAdmin (admin.ModelAdmin):
    list_display = ('pk', 'tour', 'customer', 'is_reserved')

admin.site.register(Cart, CartUserAdmin)
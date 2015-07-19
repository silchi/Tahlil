from django.contrib import admin

from .models import GlobalUser, Customer, Provider

class GlobalUserAdmin (admin.ModelAdmin):
    list_display = ('pk', 'name', 'email')

class ProviderUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_name', 'get_email', 'type')

class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_name', 'get_email')

admin.site.register(GlobalUser, GlobalUserAdmin)
admin.site.register(Provider, ProviderUserAdmin)
admin.site.register(Customer, CustomerUserAdmin)

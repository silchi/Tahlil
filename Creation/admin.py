from django.contrib import admin

from .models import Service, Tour

class ServiceUserAdmin (admin.ModelAdmin):
    list_display = ('pk', 'name', 'provider')

class TourUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'service', 'destinations', 'type')

admin.site.register(Service, ServiceUserAdmin)
admin.site.register(Tour, TourUserAdmin)
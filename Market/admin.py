from django.contrib import admin

from .models import TourTicket

class TourTicketUserAdmin (admin.ModelAdmin):
    list_display = ('pk', 'tour', 'customer', 'is_reserved')

admin.site.register(TourTicket, TourTicketUserAdmin)
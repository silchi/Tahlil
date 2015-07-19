from django.db import models

class TourTicket (models.Model):
    tour = models.ForeignKey('Creation.Tour')
    customer = models.ForeignKey('Register.Customer')
    is_reserved = models.BooleanField()
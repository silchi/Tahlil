from django.db import models

class Cart(models.Model):
    customer= models.ForeignKey('Register.Customer')
    service = models.ForeignKey('Market.TourTicket')
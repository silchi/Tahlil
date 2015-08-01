from django.db import models
from UI.util import Util

class Cart(models.Model):
    customer= models.ForeignKey('Register.Customer')
    tour = models.ForeignKey('Creation.Tour')
    is_reserved = models.BooleanField(default=False)

    def get_cost(self):
        if self.is_reserved:
            return -Util.get_reserve_cost(self.tour.service.price)
        return self.tour.service.price

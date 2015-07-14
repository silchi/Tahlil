from django.db import models
from django_enumfield import enum
from django.utils import timezone
from Register.models import Provider


class TourType(enum.Enum):
    TAFRIHI = 0
    ZAIRATI = 1
    TEJARI = 2


class Service(models.Model):
    name = models.CharField(max_length=80)
    cost = models.IntegerField()
    description = models.TextField()
    summery = models.CharField(max_length=200)
    document = models.TextField()
    capacity = models.IntegerField()
    provider = models.ForeignKey(Provider)
    sla = models.TextField()


class Hotel(models.Model):
    service = models.OneToOneField(Service)
    rate = models.IntegerField()


class Restaurant(models.Model):
    service = models.OneToOneField(Service)
    # TO DO


class Transportation(models.Model):
    service = models.OneToOneField(Service)
    # TO DO

class Tour(models.Model):
    service = models.OneToOneField(Service)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    type = enum.EnumField(TourType)
    destinations = models.TextField() # check it!
    hotel_name = models.CharField(max_length=80)
    hotel_rate = models.ImageField()
    transportation_type = models.TextField() # check it!
    transportation_company = models.CharField(max_length=80)
    duration = models.DurationField()
    from_city = models.CharField(max_length=80)
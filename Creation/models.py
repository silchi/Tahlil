# -*- coding: UTF-8 -*-
from django.db import models
#from django_enumfield import enum
from django.utils import timezone
from Register.models import Provider

TOUR_TYPE = (
    ('TAFRIHI', 'تفریحی'),
    ('ZIARATI', 'زیارتی'),
    ('TEJARI', 'تجاری'),
)

TRANSPORTATION_TYPE = (
    ('AIRPLANE','هواپیما'),
    ('TRAIN','قطار'),
    ('SHIP', 'کشتی'),
    ('BUS', 'اتوبوس'),
)

# class TourType(enum.Enum):
#     TAFRIHI = 0
#     ZAIRATI = 1
#     TEJARI = 2

class Service(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    summary = models.CharField(max_length=200)
    description = models.TextField()
    necessary_documents = models.TextField()
    capacity = models.IntegerField()
    provider = models.ForeignKey(Provider)
    sla = models.TextField()

    def __str__(self):
        return self.name + '(' + str(self.id) + ')'

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
#    type = enum.EnumField(TourType)
    type = models.CharField(max_length=10, choices=TOUR_TYPE, default='TAFRIHI')
    destinations = models.TextField() # check it!
    hotel_name = models.CharField(max_length=80)
#    hotel_rate = models.ImageField()
    # widget must be change to show stars instead of integer
    hotel_rate = models.IntegerField()
    transportation_type = models.CharField(max_length=20, choices=TRANSPORTATION_TYPE)
    transportation_company = models.CharField(max_length=80)
    duration = models.DurationField()
    from_city = models.CharField(max_length=80)

    def __str__(self):
        return self.service.name + '(' + str(self.pk) + ')'
    # def number_of_buyers(self):
    #     return MemberTourRelation.objects.filter(tour=self).__len__()
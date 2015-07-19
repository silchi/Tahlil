# -*- coding: UTF-8 -*-
from django.db import models
#from django_enumfield import enum
from django.utils import timezone
from django.contrib.auth.models import User

# class Province(enum.Enum):
#     ISFAHAN = 0
#     TEHRAN = 1
#     SHIRAZ = 2
#     TABRIZ = 3
#     MASHHAD = 4

PROVINCES = (
    ('ISFAHAN', 'اصفهان'),
    ('TEHRAN', 'تهران'),
    ('FARS', 'فارس'),
    ('KHORASAN-RAZAVI', 'خراسان رضوی'),
)

# class UserType(enum.Enum):
#     AGENCY = 0
#     HOTEL = 1
#     RESTAURANT = 2
#     TRANSPORT = 3

PROVIDER_TYPE = (
    ('AGENCY', 'آژانس هواپیمایی'),
    ('HOTEL', 'هتل'),
    ('RESTAURANT', 'رستوران'),
    ('TRANSPORT', 'حمل و نقل'),
)

# class Bank(enum.Enum):
#     MELLI = 1
#     MELLAT = 2
#     SADERAT = 3
#     TEJARAT = 4

BANKS = (
    ('MELLI', 'ملی'),
    ('MELLAT', 'ملت'),
    ('SADERAT', 'صادرات'),
    ('TEJARAT', 'تجارت'),
    ('SEPAH', 'سپه'),
)

class GlobalUser(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    province = models.CharField(max_length=20,choices=PROVINCES)
    address = models.TextField()
    credit = models.IntegerField()
    register_date = models.DateTimeField(default=timezone.now)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + ' ' + self.name

class Provider(models.Model):
    global_user = models.OneToOneField(GlobalUser)
    type = models.CharField(max_length=10,choices=PROVIDER_TYPE)
    register_number = models.CharField(max_length=20)
    website = models.URLField()
    bank_account = models.CharField(max_length=20)
    bank = models.CharField(max_length=20,choices=BANKS)

    def get_name(self):
        return self.global_user.name

    def get_email(self):
        return self.global_user.email

    def __str__(self):
        return str(self.id) + ' ' + self.global_user.name

class Customer(models.Model):
    global_user = models.OneToOneField(GlobalUser)
    national_code = models.CharField(max_length=10)

    def get_name(self):
        return self.global_user.name

    def get_email(self):
        return self.global_user.email

    def __str__(self):
        return str(self.id) + ' ' + self.global_user.name
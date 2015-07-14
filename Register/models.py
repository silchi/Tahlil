from django.db import models
from django_enumfield import enum
from django.utils import timezone
from django.contrib.auth.models import User


class Province(enum.Enum):
    ISFAHAN = 0
    TEHRAN = 1
    SHIRAZ = 2
    TABRIZ = 3
    MASHHAD = 4


class UserType(enum.Enum):
    AGENCY = 0
    HOTEL = 1
    RESTAURANT = 2
    TRANSPORT = 3


class Bank(enum.Enum):
    MELLI = 1
    MELLAT = 2
    SADERAT = 3
    TEJARAT = 4


class GlobalUser(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.IntegerField(max_length=15)
    province = enum.EnumField(Province)
    address = models.TextField()
    credit = models.IntegerField()
    register_date = models.DateTimeField(default=timezone.now)
    postal_code = models.IntegerField(max_length=10)


class Provider(models.Model):
    global_user = models.OneToOneField(GlobalUser)
    type = enum.EnumField(UserType)
    register_number = models.IntegerField(max_length=20)
    website = models.URLField()
    bank_account = models.IntegerField(max_length=20)
    bank = enum.EnumField(Bank)


class Customer(models.Model):
    global_user = models.OneToOneField(GlobalUser)
    national_code = models.IntegerField(max_length=10)
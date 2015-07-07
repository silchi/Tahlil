from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.query import QuerySet


class Tour(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    capacity = models.IntegerField()
    description = models.CharField(max_length=30)
    complete_description = models.CharField(max_length=200)
    # TODO document bayad avaz beshe
    document = models.CharField(max_length=50)
    agency = models.ForeignKey('Agency',related_name='tours')

    # def number_of_buyers(self):
    #     return MemberTourRelation.objects.filter(tour=self).__len__()


class Image(models.Model):
    tour = models.ForeignKey('Tour',related_name='images')
    refrence = models.CharField(max_length=50)

class Member(models.Model):
    user = models.OneToOneField(User, related_name='member')
    
#   TODO many to many field to Tour
class MemberTourRelation(models.Model):
    member = models.ForeignKey('Member')
    tour = models.ForeignKey('Tour')
    status = models.BooleanField()
    

class Agency(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    information = models.CharField(max_length=50)

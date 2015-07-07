# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

def show_profile_admin(request) :
    return render(request, "Dashboard/profile-admin.html")

def show_profile_agency(request) :
    return render(request, "Dashboard/profile-agency.html")

def show_profile_tourist(request) :
    return render(request, "Dashboard/profile-tourist.html")
from django.shortcuts import render

# Create your views here.

def show_register_tourist (request) :
    return render(request, "Register/register-tourist.html")

def show_register_agency (request) :
    return render(request, "Register/register-agency.html")
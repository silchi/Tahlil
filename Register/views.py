from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def show_register_tourist(request):
    return render(request, 'Register/register-tourist.html')

def show_register_agency(request):
    return render(request, 'Register/register-agency.html')

# TODO
# only for test
def do_login(request):
    # name = request.POST.get('inputEmail', '')
    # password = request.POST.get('inputPassword', '')
    # user = authenticate(username=name, password=password)
    # if user is not None:
    #     login(request, user)
    #     return HttpResponseRedirect('/home/')
    # else:
    #     return HttpResponseRedirect('/home/')
    user = authenticate(username = 'customer', password='a')
    login(request, user)
    return HttpResponseRedirect('/home/')

def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

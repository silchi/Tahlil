from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def show_home(request):
    # only for test
    # if User.objects.count() == 0:
    #     user = User.objects.create_user(username='test', password='test')
    #     user.save()
    # only for test
    # if request.user.is_authenticated() is False:
    #     user = authenticate(username='test', password='test')
    #     login(request,user)
    #     return HttpResponseRedirect('/home/')
    print(User.objects.count())
    user = request.user
    print(user.username)
    return render(request, 'UI/index.html', {'user': user})
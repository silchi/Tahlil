from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EditForm
from Market.models import TourTicket
from UI.util import Util

def show_profile(request):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home')
    elif user.is_superuser:
        return render(request, 'Dashboard/profile-admin.html')
#    elif user.is_staff:
#        return render(request, 'Dashboard/profile-agency.html')
    elif user.is_staff is True or user.is_staff is False:
        form = EditForm(request.POST)
        if request.method == 'POST':
            print('post is called')
            if form.is_valid():
                print('HERE')
                current_password = form.cleaned_data.get('current_password')
                if user.password == current_password:
                    return HttpResponseRedirect('/domestic/')
                else:
                    return HttpResponseRedirect('/home/')
            else:
                return render(request, 'Dashboard/profile-agency.html', {'user': user, 'form': form})
        else:
            print ('get is called')
            form = EditForm()
        tour_list = TourTicket.objects.filter(customer__pk = user.globaluser.provider.pk)
        print(tour_list)
        return render(request, 'Dashboard/profile-agency.html', {'user': user, 'form': form, 'tour_list': tour_list})
    else:
        form = EditForm(request.POST)
        if request.method == 'POST':
            print('post is called')
            if form.is_valid():
                print('HERE')
                current_password = form.cleaned_data.get('current_password')
                if user.password == current_password:
                    return HttpResponseRedirect('/domestic/')
                else:
                    return HttpResponseRedirect('/home/')
            else:
                return render(request, 'Dashboard/profile-tourist.html', {'user': user, 'form': form})
        else:
            print ('get is called')
            form = EditForm()
        tour_list = TourTicket.objects.filter(customer__pk = user.globaluser.customer.pk)
        print(tour_list)
        return render(request, 'Dashboard/profile-tourist.html', {'user': user, 'form': form, 'tour_list': tour_list})

def cancel(request, ticket_id):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    tour_ticket = TourTicket.objects.get(pk=ticket_id)
    if tour_ticket is None:
        return HttpResponseRedirect('/home/')
    if tour_ticket.customer.global_user.user.id is not user.id:
        return HttpResponseRedirect('/home/')
    user.globaluser.credit += Util.get_cancel_cost(tour_ticket.tour.service.price)
    user.globaluser.save()
    tour_ticket.delete()
    return HttpResponseRedirect('/profile/')

def confirm(request, ticket_id):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    tour_ticket = TourTicket.objects.get(pk=ticket_id)
    if tour_ticket is None:
        return HttpResponseRedirect('/home/')
    if tour_ticket.customer.global_user.user.id is not user.id:
        return HttpResponseRedirect('/home/')
    user.globaluser.credit += Util.get_confirm_cost(tour_ticket.tour.service.price)
    user.globaluser.save()
    tour_ticket.is_reserved = False
    tour_ticket.save()
    return HttpResponseRedirect('/profile/')
from django.shortcuts import render
from .models import Cart
from django.http import HttpResponseRedirect
from Market.models import TourTicket

def cart(request):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    if user.is_staff or user.is_superuser:
        return HttpResponseRedirect('/home/')
    cart_list = Cart.objects.filter(customer__pk = request.user.globaluser.customer.pk)
    if cart_list.count() == 0:
        return render(request, 'Financial/empty-cart.html')
    total_cost = 0
    for cart_item in cart_list:
        total_cost += cart_item.get_cost()
    return render(request, 'Financial/cart.html', {'cart_list': cart_list, 'total_cost': total_cost})

def cancel(request, ticket_id):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    cart_item = Cart.objects.get(pk=ticket_id)
    if cart_item is None:
        return HttpResponseRedirect('/home/')
    if cart_item.customer.global_user.user.id is not user.id:
        return HttpResponseRedirect('/home/')
    cart_item.delete()
    return HttpResponseRedirect('/cart/')

def confirm(request, ticket_id):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    cart_item = Cart.objects.get(pk=ticket_id)
    if cart_item is None:
        return HttpResponseRedirect('/home/')
    if cart_item.customer.global_user.user.id is not user.id:
        return HttpResponseRedirect('/home/')
    cart_item.is_reserved = False
    cart_item.save()
    return HttpResponseRedirect('/cart/')

def reserve(request, ticket_id):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    cart_item = Cart.objects.get(pk=ticket_id)
    if cart_item is None:
        return HttpResponseRedirect('/home/')
    if cart_item.customer.global_user.user.id is not user.id:
        return HttpResponseRedirect('/home/')
    cart_item.is_reserved = True
    cart_item.save()
    return HttpResponseRedirect('/cart/')

def buy(request):
    print('here in buy')
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home/')
    if user.is_staff or user.is_superuser:
        return HttpResponseRedirect('/home/')
    cart_list = Cart.objects.filter(customer__pk = request.user.globaluser.customer.pk)
    total_cost = 0
    print('salaam')
    for cart_item in cart_list:
        total_cost += cart_item.get_cost()
        tour_ticket = TourTicket(tour=cart_item.tour,customer=cart_item.customer,is_reserved=cart_item.is_reserved)
        tour_ticket.save()
        cart_item.delete()
    user.globaluser.credit -= total_cost
    user.globaluser.save()
    return HttpResponseRedirect('/home/')

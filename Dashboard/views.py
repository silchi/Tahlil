from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EditForm
from Market.models import TourTicket
from Register.models import Customer

def show_profile(request):
    user = request.user
    if user.is_authenticated() is False:
        return HttpResponseRedirect('/home')
    elif user.is_superuser:
        return render(request, 'Dashboard/profile-admin.html')
    elif user.is_staff:
        return render(request, 'Dashboard/profile-agency.html')
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
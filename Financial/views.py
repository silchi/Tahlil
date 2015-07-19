from django.shortcuts import render

# Create your views here.

def show_buy(request):
    return render(request, "Financial/buy.html")

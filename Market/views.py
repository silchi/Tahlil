from django.shortcuts import render

# Create your views here.
from Market.models import Tour, Agency, Image


def show_tour(request) :
    tour1 = Tour.objects.get(id = 1)

    return render(request, "Market/product.html", {
        'tour':tour1,
        'first_image':"http://www.winkler.fr/media/catalog/product/cache/1/image/940x/040ec09b1e35df139433887a97daa66f/4/6/4669_A.jpg",
        'isAvailable':True
    })

def show_domestic (request) :
    return render(request, "Market/domestic.html")

def show_international (request) :
    return render(request, "Market/international.html")

def show_hotels (request) :
    return render(request, "Market/hotels.html")

def show_restaurants (request) :
    return render(request, "Market/restaurants.html")

def show_transportation (request) :
    return render(request, "Market/transportation.html")
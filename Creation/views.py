from django.shortcuts import render

# Create your views here.

def definition_tour(request) :
    return render(request, "Creation/defenition-tour.html")
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def map(request):
    return render(request, 'map.html')
def home(request):
    return render(request, 'home.html')
def Apollo(request):
    return render(request, 'Apollo.html')
def SShyderabad(request):
    return render(request, 'SShyderabad.html')
def Ovenstorypizza(request):
    return render(request, 'Ovenstorypizza.html')
def WashermenpetMetro(request):
    return render(request, 'WashermenpetMetro.html')
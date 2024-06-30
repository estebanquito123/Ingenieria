from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'OnTour/index.html', context)

def servicios(request):
    context={}
    return render(request,'OnTour/servicios.html', context)

def nosotros(request):
    context={}
    return render(request,'OnTour/nosotros.html', context)

def login(request):
    context={}
    return render(request,'OnTour/login.html', context)
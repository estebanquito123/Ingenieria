from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistroForm
from django.views.decorators.csrf import csrf_protect

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

def perfil(request):
    context={}
    return render(request,'OnTour/perfil.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirige a la página de inicio o a la que desees
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def aprendijzaje(request):
    context={}
    return render(request,'OnTour/aprendizaje.html', context)

def imperdibles(request):
    context={}
    return render(request,'OnTour/imperdibles.html', context)

def exit(request):
    logout(request)
    return redirect('/')

@csrf_protect
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('/')  # Redirige a la página principal después del registro
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistroForm

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

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'¡Tu cuenta ha sido creada! Ahora estás logueado como {username}')
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


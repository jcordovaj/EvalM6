from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from vehiculo.models import Vehiculo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django import forms
from django.urls import reverse
# Librerías para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

def index(request):
    context = {
        'titulo': 'Catálogo de Vehículos',
        'vehiculos': data_vehiculos,
    }

    return render(request, 'index.html', context)

# Galería de ofertas
data_vehiculos = [
    {"id": 1, "nombre": "Fiat Punto",         "imagen": "imgs/fiat_punto.png", "descripcion": "El compacto ideal para la ciudad!!"},
    {"id": 2, "nombre": "Fiat Ducato",        "imagen": "imgs/fiat_ducato.png", "descripcion": "Llévelo hoy, trabaje mañana..."},
    {"id": 3, "nombre": "Ford F-150",         "imagen": "imgs/ford_f150.png", "descripcion": "Para quienes gustan de la aventura..."},
    {"id": 4, "nombre": "Toyota 4Runner",     "imagen": "imgs/4runner.png", "descripcion": "Excelente oferta, a toda prueba..."},
    {"id": 5, "nombre": "Chevrolet Corvette", "imagen": "imgs/chevrolet_corvette.png", "descripcion": "Si lo soñó de niño, hágalo realidad hoy..."},
]

@login_required(login_url='/usuarios/login/')
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'listar.html', context)

def exit(request):
    logout(request)
    return redirect('/')
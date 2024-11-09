from django.http import HttpResponse
from django.forms import ValidationError
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from vehiculo.models import Vehiculo
from .forms import RegistroUsuarioForm, LoginUsuarioForm

# Create your views here.

def index_view(request):
    usuarios = User.objects.all()
    for usuario in usuarios:
        usuario.groups_list = usuario.groups.values_list('name', flat=True)
        usuario.permissions_list = usuario.user_permissions.values_list('name', flat=True)    
    return render(request, 'usuarios/usuarios_view.html', {'usuarios': usuarios})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirigir al usuario después de iniciar sesión
            return redirect('index')  # Reemplaza 'home' con la URL de tu página de inicio
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login_view.html', {'form': form})

def registro_view(request):
    form = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Usuarios_std')
            user.groups.add(group)
            permission = Permission.objects.get(codename='visualizar_catalogo')
            # Asignar el permiso al usuario
            user.user_permissions.add(permission)
            login(request, user)
            messages.success(request, f"Usuario {user.username} registrado con éxito.")
            return HttpResponseRedirect("/")
        else:
            form = RegistroUsuarioForm()
            messages.error(request, "Error al intentar registrar al usuario, por favor verifique los datos.")
            return render(request, 'usuarios/registro_view.html', {"form": form})
                
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro_view.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

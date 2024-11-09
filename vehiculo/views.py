from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import permission_required
# Create your views here.

@login_required(login_url='/usuarios/login/')
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  # Luego de grabar, redirecciona al 'index.html
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/add_vehiculo.html', {'form': form})

@login_required(login_url='/usuarios/login/')
@permission_required('vehiculos.visualizar_catálogo', raise_exception=True)
def agregar_crud_vehiculo(request):
    if request.method == 'POST':
        # Se capturan los datos desde el formulario
        year              = request.POST.get('year')
        marca             = request.POST.get('marca')
        modelo            = request.POST.get('modelo')
        serial_carroceria = request.POST.get('serial_carroceria')
        serial_motor      = request.POST.get('serial_motor')
        categoria         = request.POST.get('categoria')
        precio            = request.POST.get('precio')
        descripcion       = request.POST.get('descripcion')       
        
	# Crear un nuevo objeto Vehiculo
        vehiculo = Vehiculo(year=year, marca=marca, modelo=modelo, serial_carroceria=serial_carroceria, serial_motor=serial_motor, categoria=categoria, precio=precio, descripcion=descripcion)
        vehiculo.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

# ELIMINAR VEHICULO
class VehiculoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Vehiculo
    template_name = "vehiculos/delete_vehiculo.html"
    success_url = reverse_lazy('listar')
    permission_required = 'vehiculo.delete_vehiculo'
    
    def get_object(self):
        # Obtener el objeto Vehiculo basado en la PK de la URL
        return Vehiculo.objects.get(pk=self.kwargs['pk'])   
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "No dispone de permisos para eliminar registros.")
            return redirect("index")
        
        else:
            messages.info(self.request, "Para borrar un registro, primero inicie sesión.")
            return redirect("login")
        
# EDITAR VEHICULO
class VehiculoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Vehiculo
    template_name = "vehiculos/update_vehiculo.html"
    fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'year', 'descripcion', 'precio']
    
    success_url = reverse_lazy('listar')
    permission_required = 'vehiculo.can_edit_vehiculo'
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "No dispone de permisos para eliminar registros.")
            return redirect("index")
        
        else:
            messages.info(self.request, "Para editar un registro, primero inicie sesión.")
            return redirect("usuarios/login_view")
    



from django.contrib import admin
from .models import Vehiculo
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Vehiculo)

# Para mostrar campos personalizados o buscar por ciertos campos, se crea una clase
#from@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display  = ('marca', 'modelo', 'precio')  # Campos a mostrar en la lista, sólo algunos campos 
    search_fields = ('marca', 'modelo')            # Campos para buscar, sólo por estos campos, por ejemplo los indexados


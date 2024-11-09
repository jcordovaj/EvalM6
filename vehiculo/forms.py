from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        #campos = ['year', 'marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'descripcion']
        fields = "__all__" #-> incluir todos los atributos del modelo
        # exclude = ['direccion'] -> no incluir los atributos que queremos
        
        
        #widgets = {
        #    'year'             : forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'value': 9999, 'min': 1900}),
        #    'marca'            : forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        #    'modelo'           : forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        #    'serial_carroceria': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'value': 9999999, 'min': 1}),
        #    'serial_motor'     : forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'value': 0, 'min': 0}),
        #    'categoria'        : forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        #    'precio'           : forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'value': 999999999, 'min': 1}),
        #    'descripcion'      : forms.Textarea(attrs={'class': 'form-control', 'required': 'required', 'rows': 3}),
        #}

#Year, Marca, Modelo, Serial Carrocería, Serial Motor, Categoría, Precio, Fecha de creación, Fecha de modificación, descripcion
        
        
        
        
    
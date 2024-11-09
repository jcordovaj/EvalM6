from django import forms

class CotizacionForm(forms.Form):
    nombre   = forms.CharField(max_length=100)
    email    = forms.EmailField()
    mensaje = forms.CharField(max_length=200)
    
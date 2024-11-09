from django.shortcuts import render

from cotizacion.models import Cotizacion
from .forms import CotizacionForm
from django.core.mail import send_mail

# Create your views here.

#def cotizacion(request):
#    if request.method == 'POST':
#        form = CotizacionForm(request.POST)
#        if form.is_valid():
#            # Datos del solicitante
#            nombre = form.cleaned_data['nombre']
#            email = form.cleaned_data['email']
#            mensaje = form.cleaned_data['mensaje']

            # Enviar correo
#            send_mail(
#                'Solicitud de cotización',
#                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
#                'tu_correo@example.com',
#                ['tu_correo@example.com'],
#                fail_silently=False,
#            )

#            return render(request, 'cotizacion/gracias.html')  # Redirige a una página de agradecimiento
#        else:
#            return render(request, 'cotizacion/cotizacion.html', {'form': form})
#    else:
#        form = CotizacionForm()
#       return render(request, 'cotizacion/cotizacion.html', {'form': form})
    
def cotizacion(request):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            # Crear una instancia del modelo Cotizacion
            cotizacion = Cotizacion(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )
            cotizacion.save()

            # Enviar correo
            try:
                send_mail(
                    
                )
            except Exception as e:
                # Manejar el error, por ejemplo, registrarlo en un log
                print(f"Error al enviar el correo: {e}")

            return render(request, 'cotizacion/gracias.html')
        else:
            return render(request, 'cotizacion/cotizacion.html', {'form': form})
    else:
        form = CotizacionForm()
        return render(request, 'cotizacion/cotizacion.html', {'form': form})    
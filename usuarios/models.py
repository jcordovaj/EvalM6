from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.


#class User(AbstractUser, PermissionsMixin):
    # Tus campos personalizados si los tienes

#    class Meta:
#        verbose_name        = 'Usuario'
#        verbose_name_plural = 'Usuarios'

    # Crea el permiso
#    user.add_permission(
#        codename='visualizar_catalogo',
#        name='Puede visualizar el catálogo de vehículos',
#        content_type=ContentType.objects.get(app_label='tu_app', model='Vehiculo'))
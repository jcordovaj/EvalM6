from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
        ('Chevrolet', 'Chevrolet'),
        ("Alfa Romeo", "Alfa Romeo"),
        ("Audi", "Audi"),
        ("BMW", "BMW"),
        ("Changan", "Changan"),
        ("Hyundai", "Hyundai"),
        ("Kia", "Kia"),
        ("Mazda", "Mazda"),
        ("Mercedes Benz", "Mercedes Benz"),
        ("MG Motors", "MG Motors"),
        ("Mitsubishi", "Mitsubishi"),
        ("Nissan", "Nissan"),
        ("Peugeot", "Peugeot"),
        ("Suzuki", "Suzuki"),
        ("Volkswagen", "Volkswagen"),
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    marca              = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo             = models.CharField(max_length=100)
    serial_carroceria  = models.CharField(max_length=50)
    serial_motor       = models.CharField(max_length=50)
    categoria          = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio             = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    descripcion        = models.CharField(max_length=255, default="")
    year               = models.IntegerField(default=2024)

    
    class Meta:
        permissions = (
            ("visualizar_catalogo", "Puede ver los vehículos"),
            ("can_add_vehiculo_model", "Can add vehículo model"),
        )
        
    def __str__(self):
        return self.modelo
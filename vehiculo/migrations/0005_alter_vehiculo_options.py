# Generated by Django 5.1.2 on 2024-11-08 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': (('visualizar_catalogo', 'Puede ver los vehículos'), ('can_add_vehiculo_model', 'Can add vehículo model'))},
        ),
    ]

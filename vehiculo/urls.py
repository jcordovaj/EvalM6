from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_vehiculo, name='add_vehiculo'),
    #path('crud/', views.agregar_crud_vehiculo, name='agregar_crud_vehiculo'),
    path('delete_vehiculo/<int:pk>/', views.VehiculoDeleteView.as_view(), name='delete_vehiculo'),
    path('update_vehiculo/<int:pk>/', views.VehiculoUpdateView.as_view(), name='update_vehiculo'),
    #path('vehiculos/delete/<int:pk>', views.VehiculoDeleteView.as_view(), name='delete_vehiculo'),
    #path('vehiculos/update/<int:pk>', views.VehiculoUpdateView.as_view(), name='update_vehiculo'),
    
]
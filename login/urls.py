from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='usuarios_view'),
    path('', views.login, name='login'),
            
]


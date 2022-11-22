from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lista_paciente'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciar_sesion')
]


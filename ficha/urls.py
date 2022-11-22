from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lista_paciente'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciar_sesion'),
    path('registrarse/', views.registartse, name='registrarse'),
    path('main/', views.main, name='main'),
    path('mainFuncionario/', views.mainFuncionario, name='mainFuncionario'),
    path('ficha/', views.ficha, name='ficha'),
]


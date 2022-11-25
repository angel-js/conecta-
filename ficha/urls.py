from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='lista_paciente'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciar_sesion'),
    path('registrarse/', views.registarse, name='registrarse'),
    path('main/', views.main, name='main'),
    path('mainFuncionario/', views.mainFuncionario, name='mainFuncionario'),
    path('ficha/', views.ficha, name='ficha'),
    #Vistas API
    #path('fichaID/', views.UsuarioRegistro.as_view(), name='fichas_list'),
    path('busqueda/', views.busqueda_ficha, name="busqueda_ficha"),
    path('buscar/', views.buscar, name="buscar"),
    path('agregar_paciente/', views.agregar_paciente, name="agregar"),
]


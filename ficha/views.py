from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ast import Delete
from django.contrib import messages
from django.contrib.auth import login
import json
from .forms import PacienteRegistro, UsuarioRegistro


# Create your views here.
def home(request):
    return render(request, "index.html")

def iniciarsesion(request):
    return render(request, "ficha/sesion/iniciar_sesion.html")

def registarse(request):
    return render(request, "ficha/sesion/registrarse.html")


def main(request):
    return render(request, "ficha/vistaFamiliar/main.html")

def mainFuncionario(request):
    return render(request, "ficha/vista/mainFuncionario.html")

def ficha(request):
    return render(request, "ficha.html")

#Busqueda
def busqueda_ficha(request):
    return render(request, "ficha/vistafuncionario/mainFuncionario.html") 

def buscar(request):
    if request.GET["ficha_paciente"]:
        #message="Paciente Buscado: %r" %request.GET["ficha_paciente"]
        ficha=request.GET["ficha_paciente"]
        
        if len(ficha) > 20:
            message="Texto demasiado largo"
        else:
            paciente=Usuario.objects.filter(nombre__icontains=ficha)
            return render(request, "ficha/vistafuncionario/resultados_busquedas.html",{"paciente": paciente, "query":ficha})
    else:
        message="No has introducido nada!"
    return HttpResponse(message)


# Video
def agregar_paciente(request):

    data = {
        'form': PacienteRegistro(),
    }

    if request.method == 'POST':
        formulario = PacienteRegistro(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'ficha/paciente/agregar.html', data)
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def iniciarsesion(request):
    return render(request, "iniciar_sesion.html")


def registartse(request):
    return render(request, "registrarse.html")

def main(request):
    return render(request, "main.html")

def mainFuncionario(request):
    return render(request, "mainFuncionario.html")

def ficha(request):
    return render(request, "ficha.html")
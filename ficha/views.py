from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, "index.html")

def iniciarsesion(request):
    return render(request, "iniciar_sesion.html")

def registarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'Usuario {username} creado!')
        else:
            form = UserCreationForm()
        context = {'form': form}
    return render(request, "registrarse.html")


def main(request):
    return render(request, "main.html")

def mainFuncionario(request):
    return render(request, "mainFuncionario.html")

def ficha(request):
    return render(request, "ficha.html")
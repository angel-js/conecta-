from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View


# Create your views here.
def home(request):
    return render(request, "index.html")

def iniciarsesion(request):
    return render(request, "iniciar_sesion.html")

def registarse(request):
    return render(request, "registrarse.html")


def main(request):
    return render(request, "main.html")

def mainFuncionario(request):
    return render(request, "mainFuncionario.html")

def ficha(request):
    return render(request, "ficha.html")

class FichaView(View):

    def get(self,request):
        fichas = list(Ficha.objects.values())
        if len(fichas)>0:
            datos={'message': "Success", 'fichas': fichas}
        else:
            datos= {'message': "Fichas not found...."}
        return JsonResponse(fichas)
    
    def post(self,request):
        pass
    
    def put(self,request):
        pass

    def delete(self,request):
        pass
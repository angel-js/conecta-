from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def iniciarsesion(request):
    return render(request, "iniciar_sesion.html")
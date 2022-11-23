from django import forms
from .models import Paciente, Usuario

class PacienteRegistro(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'

class UsuarioRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
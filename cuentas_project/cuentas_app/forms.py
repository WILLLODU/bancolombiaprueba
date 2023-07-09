from django import forms
from .models import Cliente, Cuenta, ClaveDinamica

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'region', 'edad']

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['num_cuenta', 'estado', 'saldo', 'fecha_apertura']

class ClaveDinamicaForm(forms.ModelForm):
    class Meta:
        model = ClaveDinamica
        fields = ['correo', 'celular']

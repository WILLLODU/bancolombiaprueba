from django.db import models

class Cliente(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    num_cuenta = models.CharField(max_length=20, primary_key=True)
    cedula_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas')
    estado = models.IntegerField(choices=[(0, 'Inactiva'), (1, 'Activa')])
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apertura = models.DateField()

    def __str__(self):
        return self.num_cuenta

class ClaveDinamica(models.Model):
    cedula_cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True, related_name='clavedinamica')
    correo = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.cedula_cliente.nombre



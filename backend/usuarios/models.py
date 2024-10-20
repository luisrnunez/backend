# venta/models.py
from django.db import models

class Proveedor(models.Model):
    nombreEmpresa = models.CharField(max_length=50)
    nombreEmpleado = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreEmpresa

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    direccion = models.TextField(blank=True, null=True)
    fecha_contratacion = models.DateField()
    fin_contratacion = models.DateField()
    activo = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

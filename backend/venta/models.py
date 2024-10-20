# usuarios/models.py
from django.db import models
from inventario.models import Producto, TipoPresentacion
from usuarios.models import Empleado

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='ventas')

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    presentacion = models.ForeignKey(TipoPresentacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.cantidad} {self.presentacion.nombre} de {self.producto.nombre}"

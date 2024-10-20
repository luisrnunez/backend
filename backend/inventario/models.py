from django.db import models
from usuarios.models import Proveedor
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    #idproveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    codigodebarra = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

  
class TipoPresentacion(models.Model):
    nombre = models.CharField(max_length=50)
    factor_conversion = models.IntegerField(help_text="6 para six-pack, 24 para caja.")
    
    def __str__(self):
        return self.nombre

class ProductoPresentacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='presentaciones')
    presentacion = models.ForeignKey(TipoPresentacion, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio de venta de la presentación.")
    stock = models.IntegerField(default=0, help_text="Cantidad disponible en esta presentación.")

    class Meta:
        unique_together = ('producto', 'presentacion')

    def __str__(self):
        return f"{self.producto.nombre} - {self.presentacion.nombre}"

    
class Compra(models.Model):
    idproveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)
    total_compra = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Total de la compra

    def __str__(self):
        return f"Compra de {self.idproveedor.nombreEmpresa} - {self.fecha_ingreso}"

  
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    presentacion = models.ForeignKey(TipoPresentacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)  # Precio al que se compró
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)  # Precio al que se venderá

    def __str__(self):
        return f"{self.cantidad} {self.presentacion.nombre} de {self.producto.nombre}"
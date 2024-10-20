# venta/views.py
from rest_framework import viewsets
from .models import Proveedor, Empleado
from .serializers import ProveedorSerializer, EmpleadoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

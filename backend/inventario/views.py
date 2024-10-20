# inventario/views.py
from rest_framework import viewsets
from .models import Producto, TipoPresentacion, ProductoPresentacion, Compra, DetalleCompra
from .serializers import ProductoSerializer, TipoPresentacionSerializer, ProductoPresentacionSerializer, CompraSerializer, DetalleCompraSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoPresentacionViewSet(viewsets.ModelViewSet):
    queryset = TipoPresentacion.objects.all()
    serializer_class = TipoPresentacionSerializer

class ProductoPresentacionViewSet(viewsets.ModelViewSet):
    queryset = ProductoPresentacion.objects.all()
    serializer_class = ProductoPresentacionSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer

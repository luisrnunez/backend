# inventario/serializers.py
from rest_framework import serializers
from .models import Producto, TipoPresentacion, ProductoPresentacion, Compra, DetalleCompra



class TipoPresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPresentacion
        fields = '__all__'

class ProductoPresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPresentacion
        fields = ['presentacion', 'precio', 'stock']

class ProductoSerializer(serializers.ModelSerializer):
    # Aquí definimos el serializer anidado para las presentaciones
    #presentaciones = ProductoPresentacionSerializer(many=True)
    print(serializers.ModelSerializer.get_field_names)
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'codigodebarra', 'activo']
        print(Producto)
    def create(self, validated_data):
        # Aquí puedes personalizar cómo se maneja la creación de un producto
        producto = Producto.objects.create(**validated_data)
        return producto


class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'presentacion', 'cantidad', 'precio_compra', 'precio_venta']


class CompraSerializer(serializers.ModelSerializer):
    detalles = DetalleCompraSerializer(many=True)  # Anidamos el serializer de DetalleCompra

    class Meta:
        model = Compra
        fields = ['id', 'idproveedor', 'fecha_ingreso', 'total_compra', 'detalles']

    def create(self, validated_data):
        # Extraemos los datos de los detalles de compra anidados
        detalles_data = validated_data.pop('detalles')

        # Creamos la compra primero
        compra = Compra.objects.create(**validated_data)

        # Creamos los detalles de compra asociados a la compra
        for detalle_data in detalles_data:
            DetalleCompra.objects.create(compra=compra, **detalle_data)

        return compra
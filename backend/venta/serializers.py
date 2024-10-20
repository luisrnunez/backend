# usuarios/serializers.py
from rest_framework import serializers
from .models import Venta, DetalleVenta

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'presentacion', 'cantidad', 'precio', 'subtotal']

class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = ['fecha', 'total', 'empleado','detalles']
    def create(self, validated_data):
        # Extraemos los datos de los detalles de venta anidados
        detalles_data = validated_data.pop('detalles')

        # Creamos la compra primero
        venta = Venta.objects.create(**validated_data)

        # Creamos los detalles de compra asociados a la compra
        for detalle_data in detalles_data:
            DetalleVenta.objects.create(venta=venta, **detalle_data)

        return venta

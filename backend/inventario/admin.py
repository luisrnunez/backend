from django.contrib import admin
from .models import Producto, ProductoPresentacion

class ProductoPresentacionInline(admin.TabularInline):
    model = ProductoPresentacion
    extra = 1  # Número de formularios adicionales vacíos

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigodebarra', 'activo']
    inlines = [ProductoPresentacionInline]

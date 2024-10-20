# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inventario/', include('inventario.urls')),
    path('api/venta/', include('venta.urls')),
    path('api/usuarios/', include('usuarios.urls')), 
]

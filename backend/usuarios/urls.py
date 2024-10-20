# venta/urls.py
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, EmpleadoViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'empleados', EmpleadoViewSet)

urlpatterns = router.urls

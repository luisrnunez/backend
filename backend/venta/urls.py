# usuarios/urls.py
from rest_framework.routers import DefaultRouter
from .views import VentaViewSet, DetalleVentaViewSet

router = DefaultRouter()
router.register(r'ventas', VentaViewSet)
urlpatterns = router.urls

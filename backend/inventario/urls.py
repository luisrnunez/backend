# inventario/urls.py
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, TipoPresentacionViewSet, ProductoPresentacionViewSet, CompraViewSet, DetalleCompraViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'tipo_presentaciones', TipoPresentacionViewSet)
router.register(r'compras', CompraViewSet)

urlpatterns = router.urls

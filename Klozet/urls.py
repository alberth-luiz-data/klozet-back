from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from clientes.views import ClienteViewSet
from estoque.views import PecaViewSet
from reservas.views import ReservaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pecas', PecaViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
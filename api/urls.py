from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ManufacturerViewSet, MaterialViewSet, ProductViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet, ReviewViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

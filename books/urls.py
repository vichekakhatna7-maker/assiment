from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CustomerViewSet,
    EmployeeViewSet,
    ItemViewSet,
    SaleViewSet,
    SaleDetailViewSet
)

router = DefaultRouter()

router.register('customers', CustomerViewSet)
router.register('employees', EmployeeViewSet)
router.register('items', ItemViewSet)
router.register('sales', SaleViewSet)
router.register('sale-details', SaleDetailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

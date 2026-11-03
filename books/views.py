from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets

from .models import Customer, Employee, Item, Sale, SaleDetail

from .serializers import (
    CustomerSerializer,
    EmployeeSerializer,
    ItemSerializer,
    SaleSerializer,
    SaleDetailSerializer
)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetailViewSet(viewsets.ModelViewSet):
    queryset = SaleDetail.objects.all()
    serializer_class = SaleDetailSerializer
# Create your views here.
# Create your views here.

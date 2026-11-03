from rest_framework import serializers
from .models import ( Customer, Employee, Item, Sale, SaleDetail )

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "all"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "all"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "all"

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "all"

class SaleDetailSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = SaleDetail
        fields = "all"

    def get_subtotal(self, obj):
        return obj.subtotal()
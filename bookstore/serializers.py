from .models import (
    Book,Book_order,Category,Category_book,Customer,Order
)
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
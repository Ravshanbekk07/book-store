from .models import (
    Book,Book_order,Category,Category_book,Customer,Order
)
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
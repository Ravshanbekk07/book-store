from .models import (
    Book,Category,Category_book,Customer,Order,Authors,Likes
)
from rest_framework import serializers
from django.contrib.auth.models import User



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



class CategoryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category_book
        fields="__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields="__all__"

class LIkeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields="__all__"
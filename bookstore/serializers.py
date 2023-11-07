from .models import (
    Book,Category,Category_book,Customer,Order,Author
)
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password



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
        model=Author
        fields="__all__"
# class UserRegistrationSerializer(serializers.ModelSerializer):
    
#     username=serializers.CharField(max_length=200)
#     email=serializers.EmailField()
#     password=serializers.CharField(write_only=True)

#     def validate_username(self,value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError('This username is already taken')
#         return value
#     def validate_email(self,value):
#         if User.objects.filter(email=value).exists():
#              raise serializers.ValidationError('This email is already taken')
#         return value
#     def validate_password(self,value):
        
#         validate_password(value)
#         return value  
    
#     def create(self,validated_data):
#         user=User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )

#         return user
#     class Meta:
#         model=User
#         fields="__all__"
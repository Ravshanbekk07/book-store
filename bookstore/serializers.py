from .models import (
    Book,Category,Order,Authors,Likes)
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import secrets
from django.shortcuts import get_object_or_404

class GoogleSignUpSerializer(serializers.Serializer):
    def create(self, validated_data):
        password = secrets.token_urlsafe(8)
        hashed_password = make_password(password)
        user, created = User.objects.get_or_create(username=validated_data['email'[:-10]],
                                                    email=validated_data['email'], 
                                                    password=hashed_password)
        user.password = password
        return user

class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields=['id','name','description']
    def validate(self, data):
        
        name = data.get("name",None)
        if  name.isnumeric():
            raise ValidationError(
                {
                    'status':False,
                    'message':'Ijodkor nomi harflardan tashkil topishi kerak'
                }
            )
        if Authors.objects.filter(name=name).exists():
             raise ValidationError(
                {
                    'status':False,
                    'message':'bu ijodkor bazamizda mavjud'
                }
            )

        
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
    def validate(self, data):
        
        name = data.get("name",None)
        if  name.isnumeric():
            raise ValidationError(
                {
                    'status':False,
                    'message':'Kategoriya harflardan tashkil topishi kerak'
                }
            )
        if Category.objects.filter(name=name).exists():
            raise ValidationError(
                {
                    'status':False,
                    'message':'Bu kategoriya bazamizda mavjud'
                }
            )

        
        return data

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(many=True)
    class Meta:
        model=Book
        fields=['id','title','price','description','picture','e_version','created_at','updated_at',
                'active','author','category']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.author.exists():
            representation['author'] = AuthorSerializer(instance.author.all(), many=True).data
        representation['authors'] = []

        if instance.category.exists():
            representation['category']=CategorySerializer(instance.category.all(), many=True).data
        
        return representation
    

    
   
    def validate(self, data):
        
        title = data.get("title",None)
        
        if Book.objects.filter(title=title).exists():
            raise ValidationError(
                {
                    'status':False,
                    'message':'bu kitob bazamizda mavjud'
                }
            )

        
        return data


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields="__all__"
#     def validate(self, data):
        
#         name = data.get("name",None)
#         if  name.isnumeric():
#             raise ValidationError(
#                 {
#                     'status':False,
#                     'message':'Kategoriya harflardan tashkil topishi kerak'
#                 }
#             )
#         if Category.objects.filter(name=name).exists():
#             raise ValidationError(
#                 {
#                     'status':False,
#                     'message':'Bu kategoriya bazamizda mavjud'
#                 }
#             )

        
#         return data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username','email']

class OrderSerializer(serializers.ModelSerializer):
    book_details = BookSerializer(source='book', read_only=True)
    customer_id = UserSerializer(read_only=True)
    class Meta:
        model=Order
        fields=['id', 'order_date', 'status', 'book', 'customer_id','book_details']
        
        extra_kwargs = {
        'id': {'read_only': True},
        'book_details': {'read_only': True},
        'customer_id': {'read_only': True},
        'order_date': {'read_only': True},
        'status': {'read_only': True},
        
        }
    
    


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields="__all__"
    def validate(self, data):
        
        name = data.get("name",None)
        if  name.isnumeric():
            raise ValidationError(
                {
                    'status':False,
                    'message':'Ijodkor nomi harflardan tashkil topishi kerak'
                }
            )
        if Authors.objects.filter(name=name).exists():
             raise ValidationError(
                {
                    'status':False,
                    'message':'bu ijodkor bazamizda mavjud'
                }
            )

        
        return data
class LIkeSerializer(serializers.ModelSerializer):
    book_details=BookSerializer(source='book_id', read_only=True)
    class Meta:
        model=Likes
        fields=["id","time","book_id","user",'book_details']
        extra_kwargs = {
        'id': {'read_only': True},
        'time': {'read_only': True},
        'user': {'read_only': True},
        'book_details' : {'read_only': True},
        
        }



    def validate(self, data):
        user = self.context['request'].user
        book = data['book_id']
        if Likes.objects.filter(user=user,book_id=book).exists():
             raise ValidationError(
                {
                    'status':False,
                    'message':'bu kitob sevimlilarga avvaldan qo\'shilgan'
                }
            )
   
        return data
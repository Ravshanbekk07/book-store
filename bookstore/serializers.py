from .models import (
    Book,Category,Order,Authors,Likes
)
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import secrets

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


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
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
                    'message':'bu kategoriya bazamizda mavjud'
                }
            )

        
        return data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
    # def validate(self, data):
        
    #     book = data.get("book",None)
    #     customer_id = data.get("customer_id",None)
        
    #     if Order.objects.filter(book=book,customer_id=customer_id).exists():
    #         raise ValidationError(
    #             {
    #                 'status':False,
    #                 'message':'bu avval zakas qilingan'
    #             }
    #         )

        
    #     return data
    


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
    class Meta:
        model=Likes
        fields="__all__"


    def validate(self, data):
        
        book_id = data.get("book_id",None)
        user=data.get('user',None)
        if Likes.objects.filter(book_id=book_id,user=user).exists():
             raise ValidationError(
                {
                    'status':False,
                    'message':'bu kitob sevimlilarga avvaldan qo\'shilgan'
                }
            )

        
        return data
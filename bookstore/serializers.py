from .models import (
    Book,Category,Order,Authors,Likes
)
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
    def validate(self, data):
        
        title = data.get("title",None)
        if  title.isnumeric():
            raise ValidationError(
                {
                    'status':False,
                    'message':'kitob nomi harflardan tashkil topishi kerak'
                }
            )
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
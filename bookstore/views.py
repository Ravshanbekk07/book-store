from django.shortcuts import render
from .models import (
    Book,Book_order,Category,Category_book,Customer,Order
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication#,TokenAuthentication
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer

class BookList(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    def post(self,request):
        data =request.data
        user=request.user
        serializer = BookSerializer(data=data)
        if not user:
                return Response({'error':'Unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class BookDetail(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
        user=request.user
        
        if not user:
                return Response({'error':'unauthorized'},status =401)
        else:
                book=get_object_or_404(Book,id=pk)
                serializer=BookSerializer(book)
                return Response(serializer.data)
        

from django.shortcuts import render
from .models import (
    Book,Book_order,Category,Category_book,Customer,Order
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication#,TokenAuthentication
from django.shortcuts import get_object_or_404
from .serializers import (BookSerializer,CategorySerializer,CustomerSerializer,
                          OrderSerializer)

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
        
    def put(self,request,pk:int):
        user=request.user
        book=get_object_or_404(Book,id=pk)    
        serializer=BookSerializer(instance=book,data=request.data)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk:int):
        user=request.user
        book = get_object_or_404(Book,id=pk)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
        else:
            book.delete()
            return Response({"status":'deleted'})
        
class CategoryList(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)
    def post(self,request):
        user=request.user
        data=request.data
        serializer=CategorySerializer(data=data)
        if not user:
                return Response({'error':'Unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CategoryDetail(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
        user=request.user
        
        if not user:
                return Response({'error':'unauthorized'},status =401)
        else:
                category=get_object_or_404(Category,id=pk)
                serializer=CategorySerializer(category)
                return Response(serializer.data)
        
    def put(self,request,pk:int):
        user=request.user
        category=get_object_or_404(Category,id=pk)    
        serializer=CategorySerializer(instance=category,data=request.data)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk:int):
        user=request.user
        category = get_object_or_404(Category,id=pk)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
        else:
            category.delete()
            return Response({"status":'deleted'})  

class CustomerList(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        
       
        if not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        else:
            customer=Customer.objects.all()
            serializer=CustomerSerializer(customer,many=True)
            return Response(serializer.data)
class CustomerDetail(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
        user=request.user
        
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        else:
                customer=get_object_or_404(Customer,id=pk)
                serializer=CustomerSerializer(customer)
                return Response(serializer.data)
    
class OrderList(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        if not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        else:
            order=Order.objects.all()
            serializer=OrderSerializer(order,many=True)
            return Response(serializer.data)
    def post(self,request):
        data =request.data
        user=request.user
        serializer = OrderSerializer(data=data)
        if not user:
                return Response({'error':'Unauthorized'},status =401)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
from django.shortcuts import render
from .models import (
    Book,Category,Category_book,Customer,Order,Author
)
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from django.shortcuts import get_object_or_404
from .serializers import (BookSerializer,CategorySerializer,CustomerSerializer,
                          OrderSerializer,CategoryBookSerializer,AuthorSerializer,)
                          #UserRegistrationSerializer)


# class UserRegister(APIView):
   

#     def post(self,request):
#         serializer=UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user=serializer.save() 
#             token=Token.objects.get_or_create(user=user)
#             return Response({'token':token.key,'message':'user registered successfully'} ,status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class UserLogin(APIView):
    
    
    # def post(self,request):
    #     token, created = Token.objects.get_or_create(user=request.user)
    #     return Response({'token': token.key, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)  

class BookList(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated,]

    def get(self,request):
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    def post(self,request):
        data =request.data
        user=request.user
        serializer = BookSerializer(data=data)
        
        if not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class BookDetail(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

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
        
        if not user.is_superuser:
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
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)
    def post(self,request):
        user=request.user
        data=request.data
        serializer=CategorySerializer(data=data)
        # if not user:
        #         return Response({'error':'Unauthorized'},status =401)
        if not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CategoryDetail(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

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
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        
       
        if not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        else:
            customer=Customer.objects.all()
            serializer=CustomerSerializer(customer,many=True)
            return Response(serializer.data)
class CustomerDetail(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
        user=request.user
        
        # if not user:
        #         return Response({'error':'unauthorized'},status =401)
        if not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
        else:
                customer=get_object_or_404(Customer,id=pk)
                serializer=CustomerSerializer(customer)
                return Response(serializer.data)
    
class OrderList(APIView):

    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

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
class OrderDetail(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
        user=request.user
        if not user:
                return Response({'error':'unauthorized'},status =401)
        else:
                order=get_object_or_404(Order,id=pk)
                serializer=OrderSerializer(order)
                return Response(serializer.data)
        
    def put(self,request,pk:int):
        user=request.user
        order=get_object_or_404(Order,id=pk)    
        serializer=OrderSerializer(instance=order,data=request.data)
        if not user:
            return Response({'error':'Unauthorized'},status =401)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk:int):
        user=request.user
        order = get_object_or_404(Order,id=pk)
        if not user:
            return Response({'error':'Unauthorized'},status =401)
        else:
            order.delete()
            return Response({"status":'deleted'})  


class CategoryBookList(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request):
        category_booklist=Category_book.objects.all()
        serializer=CategoryBookSerializer(category_booklist,many=True)
        return Response(serializer.data)
    def post(self,request):
        data =request.data
        user=request.user
        serializer = CategoryBookSerializer(data=data)
        if not user:
                return Response({'error':'Unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'Forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
                
class CategoryBookDetail(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self,request,pk:int):
        category_booklist=get_object_or_404(Category_book,id=pk)
        serializer=CategoryBookSerializer(category_booklist)
        return Response(serializer.data)
        
    def put(self,request,pk:int):
        user=request.user
        category_booklist=get_object_or_404(Category_book,id=pk)    
        serializer=CategoryBookSerializer(instance=category_booklist,data=request.data)
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
        category_booklist = get_object_or_404(Category_book,id=pk)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
        else:
            category_booklist.delete()
            return Response({"status":'deleted'})


class AuthorList(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request):
        
        author=Author.objects.all()
        serializer=AuthorSerializer(author,many=True)
        return Response(serializer.data)
    def post(self,request):
        data =request.data
        user=request.user
        serializer = AuthorSerializer(data=data)
        
        if not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class AuthorDetail(APIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
       
       
        author=get_object_or_404(Author,id=pk)
        serializer=AuthorSerializer(author)
        return Response(serializer.data)
        
    def put(self,request,pk:int):
        user=request.user
        author=get_object_or_404(Author,id=pk)    
        serializer=AuthorSerializer(instance=author,data=request.data)
        
        if not user.is_superuser:
            return Response({'error':'Forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk:int):
        user=request.user
        author = get_object_or_404(Author,id=pk)
        
        if not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
        else:
            author.delete()
            return Response({"status":'deleted'})



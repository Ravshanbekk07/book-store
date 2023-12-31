from .models import (
    Book,Category,Order,Authors,Likes
)
from rest_framework import status,generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from django.shortcuts import get_object_or_404,render
from .serializers import (BookSerializer,CategorySerializer,
                          OrderSerializer,AuthorSerializer,LIkeSerializer,
                          GoogleSignUpSerializer,UserTokenSerializer)
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pagination import pagination

def login(request):
    return render(request,'login.html')
@login_required
def home(request):
    return render(request,'home.html')

class GoogleSignUpView(APIView):
     
    def post(self, request):
        serializer = GoogleSignUpSerializer(data=request.data)
        if serializer.is_valid():

            user = serializer.save()
            return Response({'message': 'User created successfully', 'password': user.password}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserTokenView(APIView):
    def post(self, request):
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LastBooks(APIView):
    def get(self,request):
        return Response(pagination(
            page = request.GET.get('page', 1),
            limit = request.GET.get('limit', 5),
            form=Book.objects.all()[::-1][:20],
            serializer=BookSerializer),status=200)
    
class SearchBook(APIView):
    def get(self,request):
        title=request.GET.get("title",'')
        results = Book.objects.filter(title__icontains=title)
        serializer=BookSerializer(results,many=True)
        return Response(serializer.data) 

class BookList(APIView):
   
  
    def get(self,request):
        book=Book.objects.exclude(e_version__exact='')
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if not request.user.is_superuser:
            return Response({'error':'Forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
class BookDetail(APIView):

    def get(self,request,pk:int):
        book=get_object_or_404(Book,id=pk)
        serializer=BookSerializer(book)
        return Response(serializer.data)
        
    def put(self,request,pk:int):
        book=get_object_or_404(Book,id=pk)    
        serializer=BookSerializer(instance=book,data=request.data)
        if not request.user.is_superuser:
            return Response({'error':'Forbidden'},status=403)
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk:int):
        user=request.user
        book = get_object_or_404(Book,id=pk)
        if not user.is_superuser:
            return Response({'error':'Forbidden'},status=403)
        else:
            book.delete()
            return Response({"status":'Deleted'})
        
class CategoryList(APIView):
   
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)
    # def post(self,request):
    #     serializer=CategorySerializer(data=request.data)
    #     if not request.user.is_superuser:
    #         return Response({'error':'Forbidden'},status=403)
    #     elif serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


    
class OrderList(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
     
    def get(self,request):
        if not request.user:
            return Response({'error':'Unauthorized'},status =401)
        elif request.user.is_superuser:
            order=Order.objects.all()
            serializer=OrderSerializer(order,many=True)
            return Response(serializer.data)
        else:
            order=Order.objects.filter(customer_id=request.user)
            serializer=OrderSerializer(order,many=True)
            return Response(serializer.data)
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if not request.user:
            return Response({'error':'Unauthorized'},status = 401)
        elif serializer.is_valid():
            serializer.save(customer_id=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
        

class OrderDetail(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk:int):
        if not request.user:
            return Response({'error':'Unauthorized'},status = 401)
        elif request.user.is_superuser:
            order=get_object_or_404(Order,id=pk)
            serializer=OrderSerializer(order)
            return Response(serializer.data)
        else:
            order=get_object_or_404(Order,customer_id=request.user,id=pk)
            serializer=OrderSerializer(order)
            return Response(serializer.data)
   
    def delete(self,request,pk:int):
        order=get_object_or_404(Order,id=pk)
        if not request.user:
            return Response({'error':'Unauthorized'},status = 401)
        elif not request.user.is_superuser:
            return Response({'error':'Forbidden'},status = 401)
        order.delete()
        return Response({"status":'deleted'})  

class AuthorList(APIView):
  
    def get(self,request):
        author=Authors.objects.all()
        serializer=AuthorSerializer(author,many=True)
        return Response(serializer.data)
    # def post(self,request):
    #     serializer = AuthorSerializer(data=request.data)
    #     if not request.user.is_superuser:
    #         return Response({'error':'Forbidden'},status=403)
    #     elif serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
        
# class AuthorDetail(APIView):
    
    # def get(self,request,pk:int):
    #     author=get_object_or_404(Authors,id=pk)
    #     serializer=AuthorSerializer(author)
    #     return Response(serializer.data)
        
    # def put(self,request,pk:int):
    #     author=get_object_or_404(Authors,id=pk)    
    #     serializer=AuthorSerializer(instance=author,data=request.data,partial=True)
    #     #partial=true faqatgina bazilarini update qilish uchun ishlatiladi agar modelda null=true yoki blank=true bolmasa
    #     if not request.user.is_superuser:
    #         return Response({'error':'Forbidden'},status=403)
    #     elif serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    # def delete(self,request,pk:int):
    #     author = get_object_or_404(Authors,id=pk)
    #     if not request.user.is_superuser:
    #         return Response({'error':'Forbidden'},status=403)
    #     else:
    #         author.delete()
    #         return Response({"status":'Deleted'})


class mainAuth(APIView):
     def get(self,request,pk:int):
        author = get_object_or_404(Authors,id=pk)
        books = author.books.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
        
class CategoryBookDetail(APIView):
     def get(self,request,pk:int):
        category = get_object_or_404(Category,id=pk)
        books = category.categories.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
                  

class LikeList(generics.ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    serializer_class = LIkeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Likes.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LIkeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get_queryset(self):
        return Likes.objects.filter(user=self.request.user)
    
     



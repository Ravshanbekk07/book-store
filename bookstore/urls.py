from django.urls import path
from .views import (BookList,BookDetail,CategoryList,CategoryDetail,
                    CustomerList,CustomerDetail,OrderList,OrderDetail,
                   CategoryBookList,CategoryBookDetail,AuthorList,AuthorDetail,
                   UserRegister,UserLogin)
urlpatterns=[
    path('all/',BookList.as_view()),
    path('<int:pk>/',BookDetail.as_view()),

    path('category/all/',CategoryList.as_view()),
    path('category/<int:pk>/',CategoryDetail.as_view()),

    path('customer/all/',CustomerList.as_view()),
    path('customer/<int:pk>/',CustomerDetail.as_view()),

    path('order/all/',OrderList.as_view()),
    path('order/<int:pk>/',OrderDetail.as_view()),

   

    path('categorybook/all/',CategoryBookList.as_view()),
    path('categorybook/<int:pk>/',CategoryBookDetail.as_view()),

    path('authors/all/',AuthorList.as_view()),
    path('author/<int:pk>/',AuthorDetail.as_view()),

   
    path('register/',UserRegister.as_view()),
    path('login/',UserLogin.as_view()),

]
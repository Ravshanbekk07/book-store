from django.urls import path
from .views import (BookList,BookDetail,CategoryList,CategoryDetail,
                    CustomerList,CustomerDetail
)
urlpatterns=[
    path('all/',BookList.as_view()),
    path('<int:pk>/',BookDetail.as_view()),

    path('category/all/',CategoryList.as_view()),
    path('category/<int:pk>/',CategoryDetail.as_view()),

    path('customer/all/',CustomerList.as_view()),
    path('customer/<int:pk>/',CustomerDetail.as_view()),
]
from django.urls import path
from .views import (BookList,BookDetail,CategoryList,
                    OrderList,OrderDetail,
                   AuthorList,
                   LastBooks,LikeList,LikeDetail,mainAuth,CategoryBookDetail,
                   GoogleSignUpView,CustomUserTokenView,SearchBook)
                   
from rest_framework.routers import SimpleRouter
from deletedcodes import BookViewSet


router=SimpleRouter()
router.register('allbook',BookViewSet,basename='books')

urlpatterns=[
  
    path('google-signup/', GoogleSignUpView.as_view(), name='google_sign_up'),
    path('token/',CustomUserTokenView.as_view(),name='customer_user'),
    path('all/',BookList.as_view()),
    path('<int:pk>/',BookDetail.as_view()),

    path('category/all/',CategoryList.as_view()),
   

    path('order/all/',OrderList.as_view()),
    path('order/<int:pk>/',OrderDetail.as_view()),

    path('authors/all/',AuthorList.as_view()),
   

    path('lastbooks/',LastBooks.as_view()),
   
    path('favorites/',LikeList.as_view()),
    path('favorites/<int:pk>/',LikeDetail.as_view()),

    path('mainauth/<int:pk>/',mainAuth.as_view()),
    path('categorybook/<int:pk>/',CategoryBookDetail.as_view()),

    path('search/',SearchBook.as_view()),

   
]

# urlpatterns=urlpatterns+router.urls
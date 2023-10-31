from django.shortcuts import render
from .models import (
    Book,Book_order,Category,Category_book,Customer,Order
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication#,TokenAuthentication
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,permissions

from .models import Product
from .serializers import ProductSerializer
from .models import Product_Comment
from .serializers import ProductCommentSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class ProductCommentList(generics.ListCreateAPIView):
    queryset = Product_Comment.objects.all()
    serializer_class = ProductCommentSerializer

class ProductCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_Comment.objects.all()
    serializer_class = ProductCommentSerializer
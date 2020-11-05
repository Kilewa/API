from rest_framework import  serializers
from .models import Product, Product_Comment
from django.contrib.auth.models import User



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name', 'product_image', 'category', 'price', 'description', 'pub_date')
        model = Product  

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product_Comment

from rest_framework import generics
from rest_framework import serializers
from .models import *


#SERIALIZER FOR USER
class UserSerializes(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']


#SERIALIZER FOR PRODUCT
class ProductListSerializes(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_image', 'product_title', 'product_description', 'product_price', 'product_region', 'see_later', 'product_user', 'review', 'rating']


class ProductSerializes(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


#SERIALIZER FOR ORDER
class OrderSerializes(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


#SERIALIZER FOR CATEGORY
class CategorySerializes(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


#SERIALIZER FOR RATING
class RatingSerializes(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


#SERIALIZER FOR REVIEW
class ReviewSerializes(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
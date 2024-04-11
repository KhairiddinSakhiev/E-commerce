from django.shortcuts import render
from .serializers import *
from rest_framework import generics


class UserCreateSerializes(generics.CreateAPIView):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']


class UserUpdateSerializes(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']


class UserListSerializes(generics.ListAPIView):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']


#CRUD FOR PRODUCT
class ProductListSerializes(generics.ListAPIView):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializes(generics.CreateAPIView):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializes(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Product
        fields = '__all__'


#CRUD FOR ORDER
class OrderListSerializes(generics.ListAPIView):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializes(generics.CreateAPIView):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializes(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Order
        fields = '__all__'


#CRUD FOR CATEGORY
class CategoryListSerializes(generics.ListAPIView):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializes(generics.CreateAPIView):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializes(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Category
        fields = '__all__'


#CRUD FOR RATING
class RatingListSerializes(generics.ListAPIView):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingListSerializes(generics.CreateAPIView):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingListSerializes(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Rating
        fields = '__all__'


#CRUD FOR RAVIEW
class ReviewListSerializes(generics.ListAPIView):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializes(generics.CreateAPIView):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializes(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Review
        fields = '__all__'


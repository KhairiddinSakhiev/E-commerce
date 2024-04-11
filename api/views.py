from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *


#CRUD FOR USER
class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializes


class UserUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializes


class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializes


#CRUD FOR PRODUCT
class ProductListAPI(generics.ListAPIView):

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProductFilter


class ProductCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class ProductUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


#CRUD FOR ORDER
class OrderListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class OrderCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class OrderDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


#CRUD FOR CATEGORY
class CategoryListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class CategoryCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class CategoryDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


#CRUD FOR RATING
class RatingListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class RatingCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class RatingListAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


#CRUD FOR RAVIEW
class ReviewListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class ReviewCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


class ReviewDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializes


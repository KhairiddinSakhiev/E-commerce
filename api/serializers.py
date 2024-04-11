from rest_framework import generics
from .models import *


class UserSerializes(generics.CreateAPIView):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']


class UserSerializes(generics.CreateAPIView):
    class Meta:
        model = User
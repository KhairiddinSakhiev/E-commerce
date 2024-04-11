from django.urls import path
from .views import *

urlpatterns = [
    path('list-product/', ProductListAPI.as_view()),
    path('create-product/', ProductCreateAPI.as_view()),
    path('update-product/<int:pk>/', ProductUpdateAPI.as_view()),
    path('delete-product/<int:pk>/', ProductUpdateAPI.as_view()),
    path('detail-product/<int:pk>/', ProductUpdateAPI.as_view()),
]

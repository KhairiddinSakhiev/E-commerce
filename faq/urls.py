from django.urls import path
from .views import *


urlpatterns = [
    path('questions/', CustomerQuestionListCreateAPIView.as_view(), name='question_list_create'),
    path('questions/<int:question_id>/respond/', ProductOwnerResponseCreateAPIView.as_view(), name='respond_question'),
]
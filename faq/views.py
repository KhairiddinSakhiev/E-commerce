from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import CustomerQuestionSerializer, ProductOwnerResponseSerializer
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, CreateAPIView


class CustomerQuestionListCreateAPIView(ListCreateAPIView):
    queryset = CustomerQuestion.objects.all()
    serializer_class = CustomerQuestionSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

class ProductOwnerResponseCreateAPIView(CreateAPIView):
    serializer_class = ProductOwnerResponseSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, question_id):
        question = CustomerQuestion.objects.get(pk=question_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
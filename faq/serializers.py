from rest_framework import serializers
from .models import CustomerQuestion, ProductOwnerResponse

class CustomerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuestion
        fields = "__all__"

class ProductOwnerResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOwnerResponse
        fields = '__all__'

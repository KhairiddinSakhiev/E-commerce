from django.db import models
from api.models import User


class CustomerQuestion(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    date_question = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.username} : {self.question}'

class ProductOwnerResponse(models.Model):
    question = models.OneToOneField(CustomerQuestion, on_delete=models.CASCADE)
    response = models.TextField()
    date_response = models.DateTimeField(auto_now_add=True)

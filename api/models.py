from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Product(models.Model):

    product_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    product_title = models.CharField(max_length=250)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_region = models.CharField(max_length=250)
    see_later = models.BooleanField(default=False)
    product_user = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


class Category(models.Model):

    category_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    category_title = models.CharField(max_length=250)
    category_products = models.ForeignKey(Product, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Ca tegorys")

    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Rating(models.Model):

    product_rating = models.ForeignKey(Product, related_name='rating', on_delete=models.CASCADE)
    num_of_rating = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = ("Rating")
        verbose_name_plural = ("Ratings")

    def __str__(self):
        return self.num_of_rating

    def get_absolute_url(self):
        return reverse("Rating_detail", kwargs={"pk": self.pk})


class Review(models.Model):

    product_review = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name = ("Review")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Review_detail", kwargs={"pk": self.pk})
    

class SeeLater(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("SeeLater")
        verbose_name_plural = ("SeeLaters")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SeeLater_detail", kwargs={"pk": self.pk})


class Order(models.Model):

    user_order = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    product_order = models.ForeignKey(Product, related_name='order', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
    

class Question(models.Model):

    question = models.TextField()

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("Question_detail", kwargs={"pk": self.pk})


class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions')
    asker = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    date_asked = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    date_answered = models.DateTimeField(auto_now_add=True)
    
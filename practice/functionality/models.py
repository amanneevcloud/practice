from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, related_name = 'userr')
    name = models.CharField(max_length = 250)
    email = models.EmailField(unique = True)
    address = models.TextField()
    photo = models.ImageField(upload_to = 'photo/customer')

    def __str__(self):
        return self.name


class DeliveryPartner(models.Model):
    name = models.CharField(max_length = 50)
    mobile_num = models.IntegerField()
    photo = models.ImageField(upload_to = 'photo/delivery_partner')
    active = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Product(models.Model):
    RATING = [
        ('1','One'),
        ('2','Second'),
        ('3','Three'),
    ]

    product_name =  models.CharField(max_length = 50)
    product_description =  models.CharField(max_length = 50)
    product_actual_price =  models.IntegerField()
    product_sell_price =  models.IntegerField()
    product_rating =  models.CharField(max_length = 50, choices = RATING)


class  CartItem(models.Model):
    customer = models.ForeignKey(Product,on_delete = models.CASCADE)
    cart_rate = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} {self.product_rate}"

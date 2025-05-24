from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['name','email','address','photo']




class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class Customergetserializer(serializers.ModelSerializer):
    userr = Userserializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['name','email','userr']
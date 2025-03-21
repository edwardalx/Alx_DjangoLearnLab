from .models import Book
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password']
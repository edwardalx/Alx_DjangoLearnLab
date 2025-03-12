from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, UserSerializer,User
from rest_framework import viewsets
from rest_framework.authtoken import views 
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = [BookSerializer]

class UserToken(views.ObtainAuthToken):
    ...
# class UserToken(views.ObtainAuthToken):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
from django.shortcuts import render
from .serializers import CommentSerializer, PostSerializer,Post,Comment
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class PostPagination(PageNumberPagination):
    page_size = 5  # Customize page size if needed
    page_size_query_param = 'page_size'  # Allow users to set page size
    max_page_size = 100  # Limit the maximum page size

class CommentPagination(PageNumberPagination):
    ...

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class =PostPagination
    permission_classes = IsAuthenticatedOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Comment.objects.all()
    permission_classes= IsAuthenticatedOrReadOnly
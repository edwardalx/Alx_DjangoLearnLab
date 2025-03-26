from django.shortcuts import render
from serializers import CommentSerializer, PostSerializer,Post,Comment
from rest_framework.viewsets import ModelViewSet 

# Create your views here.

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Comment.objects.all()
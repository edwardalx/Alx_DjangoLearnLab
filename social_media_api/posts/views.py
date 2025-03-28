from django.shortcuts import render
from .serializers import CommentSerializer, PostSerializer,Post,Comment
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,permission_classes

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
    permission_classes = permissions.IsAuthenticatedOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Comment.objects.all()
    permission_classes= permissions.IsAuthenticatedOrReadOnly


class PostFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        post = self.get_object.author
        following_users = post.following.all()
        Post.objects.filter(author__in=following_users).order_by(Post.created_at)
        return super().get_queryset()
#post to like  =>> get_object_or_404(Post, user_id)
#if request.user in Like.user raise error
#else add post to Like.post

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(self, request):
    ...




@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(self, request):
    ...
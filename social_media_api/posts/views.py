from django.shortcuts import render
from .serializers import CommentSerializer, PostSerializer,Post,Comment
from rest_framework import viewsets, generics
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,permission_classes
from models import Like
from notifications.models import Notification
from rest_framework.response  import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType

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
    permission_classes = permissions.IsAuthenticated

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Comment.objects.all()
    permission_classes= permissions.IsAuthenticated

class PostFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        Post.objects.filter(author__in=following_users).order_by('-created_at')
        return super().get_queryset()
    

#post to like  =>> get_object_or_404(Post, user_id)
#if request.user in Like.user raise error
#else add post to Like.post

def create_notification(recipient, actor, verb, target_object):
    """Helper function to create a notification."""
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=ContentType.objects.get_for_model(target_object),
        object_id=target_object.id
    )

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post_to_like = generics.get_object_or_404(Post, pk=pk)
    if post_to_like.author == request.user:
        return Response({'error': 'you can not like your own post'})
    like, created =Like.objects.get_or_create(user=request.user, post=post_to_like)
    if like:
        return Response({'message', 'Post Liked'}, status=status.HTTP_201_CREATED)
    Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    
    create_notification(
            recipient=post_to_like.author, 
            actor=request.user, 
            verb=f"{request.user.username} started following you.", 
            target_object=request.user
        )
    return Response({"message": f"You are now following {post_to_like.author.username}"}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    ...
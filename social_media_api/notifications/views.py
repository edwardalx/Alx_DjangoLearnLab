from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework import generics,viewsets,views
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Notification
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer

User = get_user_model()

# Create your views here.

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
def follow_user(request, user_id):
    """Allow a user to follow another user and create a notification."""
    user_to_follow = get_object_or_404(User, id=user_id)

    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)

    # Create a notification
    create_notification(
        recipient=user_to_follow, 
        actor=request.user, 
        verb=f"{request.user.username} started following you.", 
        target_object=request.user
    )

    return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class NotificationListView(views.APIView):
    
    """Fetch all notifications for the logged-in user."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class NotiListView(generics.ListAPIView):
    permission_classes =[permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    def get_queryset(self):
        queryset = Notification.objects.filter(recipient =self.request.user).order_by('-timestamp')
        return queryset


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_notification_as_read(request, notification_id):
    """Mark a notification as read."""
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()
    return Response({"message": "Notification marked as read"}, status=status.HTTP_200_OK)

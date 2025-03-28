from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    actor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='actor_notification')
    verb = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Reference to the target model (Post, Comment, etc.)
    object_id = models.PositiveIntegerField()  # ID of the object in the target model
    target = GenericForeignKey()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.recipient.username} :  {self.verb}"

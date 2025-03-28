from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
User = get_user_model()

class Notifications(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    actor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notification')
    verb = models.TextField()
    target = GenericForeignKey()
    timestamp = models.DateTimeField(auto_now_add=True)



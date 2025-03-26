from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=300, null= True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    followers = models.ManyToManyField('CustomUser', symmetrical=False)

    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name","last_name"]
    

    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)
    def __str__(self):
        return f"Name: {self.username}  Followers:{self.followers[:5]} ... "
    
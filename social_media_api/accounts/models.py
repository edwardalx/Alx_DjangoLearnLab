from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission,BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
         use_in_migrations = True
         def create_user(self, email,username=None, password=None, **extra_fields):
                if not email:
                    raise ValueError("The given username must be set")
                email = self.normalize_email(email)
                extra_fields.setdefault("is_staff", False)
                extra_fields.setdefault("is_superuser", False)
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
         
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=300, null= True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    followers = models.ManyToManyField('CustomUser', symmetrical=False, related_name='user_folllower')
    following = models.ManyToManyField('CustomUser',symmetrical=False, related_name='user_folllowing')

    

    objects = CustomUserManager()
                     
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', "first_name","last_name"]
    

    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)
    def __str__(self):
        return f"Name: {self.username}  Followers:{self.followers[:5]} ... "
    
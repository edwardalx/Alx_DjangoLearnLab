from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255,  null=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return  f"Title:{self.title} Author: {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=255, null=False)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return  f"Name:{self.name}"

class Librarian(models.Model):
    name = models.CharField(max_length=255, null=False)
    library = models.OneToOneField(Library, related_name='librarian', on_delete=models.CASCADE)
    def __str__(self):
        return  f"Name:{self.name} Library: {self.library.name}"


# User Roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create a UserProfile when a new User is registered
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

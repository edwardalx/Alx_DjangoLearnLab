from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255,  null=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

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

# class UserProfile(models.Model):
#     ROLE_CHOICES = [
#         ('Admin', 'Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

#     def __str__(self):
#         return f"{self.user.username} - {self.role}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for the profile
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
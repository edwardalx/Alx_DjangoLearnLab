from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255,  null=False)

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=255, null=False)
    books = models.ManyToManyField(Book, related_name='library')

class Librarian(models.Model):
    name = models.CharField(max_length=255, null=False)
    library = models.OneToOneField(Library, related_name='librarian', on_delete=models.CASCADE)


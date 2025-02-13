from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField() 

newbook = Book('1984' , author='George Orwell', publication_year=1949)

books = Book.objects.all()

update_title = Book.objects.update()


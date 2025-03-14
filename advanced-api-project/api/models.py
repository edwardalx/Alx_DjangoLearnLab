from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"Title: {self.title}  Year:  {self.publication_year}"
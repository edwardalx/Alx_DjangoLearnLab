from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField() 

    def __str__(self):
        return f"title : {self.title} author: {self.author} publication_year:{self.publication_year} "

newbook = Book('1984' , author='George Orwell', publication_year=1949)

books = Book.objects.all()
book = Book.objects.get(id = 1)

# update_title = Book.objects.get(id = 1)
# update_title.title = "Edward"
# update_title.save()
# print(book)


update_title = Book.objects.filter(author="George Orwell").update(title="Edward")

book = Book.objects.get(id = 1)
book.delete()


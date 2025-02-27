from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField() 

    class Meta:
        permissions = [
            ("can_create_book", "Can create book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
            ("can_view_book", "Can view book"),
        ]

    def __str__(self):
        return f"title : {self.title} author: {self.author} publication_year:{self.publication_year} "

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)
    profile_photo = models.ImageField(upload_to="profile_pics/", null=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth", "profile_photo"]


# create_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

# retrieve_books = Book.objects.get(id = 5)

# books = Book.objects.all()
# book = Book.objects.get(id = 1)

# update_title = Book.objects.get(id = 1)
# update_title.title = "Edward"
# update_title.save()
# print(book)

# book = Book.objects.get(id=1)
# book.title = "Nineteen Eighty-Four" 
# book.save()

# update_title = Book.objects.filter(author="George Orwell").update(title="Edward")

# book = Book.objects.get(id = 1)
# book.delete()


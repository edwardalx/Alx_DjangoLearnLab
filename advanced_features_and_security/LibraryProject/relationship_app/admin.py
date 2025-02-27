from django.contrib import admin

# Register your models here.
# relationship_app/admin.py

from .models import Book
from .models import Librarian
admin.site.register(Librarian)
admin.site.register(Book)
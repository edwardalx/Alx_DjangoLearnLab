from django.db import models
from relationship_app.models import Author, Book,Library, Librarian

author_name = ""
author = Author.objects.get(name=author_name)
all_books_by_author = Book.objects.filter(author=author)
for book in all_books_by_author:
    print(book.title)

library_name = ""
my_library = Library.objects.get(name=library_name)
# all_books_in_lib = Book.objects.filter(library = my_library)
all_books_in_lib = my_library.books.all()

for book in all_books_in_lib:
    print(book.title)

# librarian_for_a_Library = my_library.librarian

# print(librarian_for_a_Library.name)

my_librarian = Librarian.objects.get(name="")
librarys_librarian = my_librarian.library
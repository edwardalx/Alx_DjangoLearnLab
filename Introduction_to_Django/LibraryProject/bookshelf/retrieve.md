from bookshelf.models import Book
retrieve_books = Book.objects.get(id = 5)
for i in retrieve_books: print(i.title, i.author,i.publication_year )
1984 George Orwell 1949

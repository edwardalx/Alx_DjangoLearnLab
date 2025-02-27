from bookshelf.models import Book
create_book = Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)
print(create_book)
Book object (1)

retrieve_books = Book.objects.all() 
print(retrieve_books) 
<QuerySet [<Book: Book object (1)>]>

retrieve_book = Book.objects.get(id=1)
retrieve_book.title = "Nineteen Eighty-Four" 
print(retrieve_book.title) 
Nineteen Eighty-Four


retrieve_book = Book.objects.get(id = 1)
retrirve_book.delete
(2, {'bookshelf.Book': 2})
print(retrieve_book)
<QuerySet []>
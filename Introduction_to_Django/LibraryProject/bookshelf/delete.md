book = Book.objects.get(id = 1)
book.delete
(2, {'bookshelf.Book': 2})
print(book)
<QuerySet []>
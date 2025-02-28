from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from .models import Book
# Create your views here.

def list_book(request):
    book = Book.objects.all()
    return render(request , 'book_list.html', {'book':book})

from .forms import ExampleForm

def example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            return render(request, "form_example.html", {"name": name})
    else:
        form = ExampleForm()

    return render(request, "example_template.html", {"form": form})

    
# View to view a book
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to view a book
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    return render(request, 'create_book.html')

# View to edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit a book
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to delete a book
    return render(request, 'delete_book.html', {'book': book})


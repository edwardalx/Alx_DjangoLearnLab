from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, CreateView, v
from django.views.generic.detail import DetailView
from .models import Author, Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = 'library'  # This will be the variable name in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.object
        context['books'] = library.books.all()
        return context

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to the homepage
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(LoginView):
    template_name = 'relationship_app/logout.html'

class CustomLogoutView(View):
    template_name = 'relationship_app/logout.html'  # Specify the template name

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST requests for logout.
#         """
#         logout(request)  # Log the user out
#         return redirect('home')  # Redirect to the homepage after logout

#     def get(self, request, *args, **kwargs):
#         """
#         Handle GET requests by rendering the logout confirmation page.
#         """
# Helper functions for role checks
def user_is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Views restricted to specific roles

@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# # # Example: Accessing the profile in a view
# # def my_view(request):
# #     user = request.user
# #     if hasattr(user, 'profile'):
# #         profile = user.profile
# #     else:
# #         # Handle the case where the profile does not exist
# #         profile = None

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")  # Get author ID from form
        author = Author.objects.get(id=author_id)  # Retrieve author instance

        # Create a new book instance
        Book.objects.create(title=title, author=author)

        return redirect("list_books")  # Redirect to book list after adding

    authors = Author.objects.all()  # Get all authors for selection in form
    return render(request, "relationship_app/add_book.html", {"authors": authors})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """View to edit a book, only for users with 'can_change_book' permission."""
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")  # Get author ID from form
        author = get_object_or_404(Author, id=author_id)  # Ensure author exists

        # Update book details
        book.title = title
        book.author = author
        book.save()

        return redirect('book_list')  # Redirect after updating

    authors = Author.objects.all()  # Get all authors for dropdown
    return render(request, 'relationship_app/edit_book.html', {"book": book, "authors": authors})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """View to delete a book, only for users with 'can_delete_book' permission."""
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect('book_list')

    return render(request, 'relationship_app/delete_book.html', {"book": book})
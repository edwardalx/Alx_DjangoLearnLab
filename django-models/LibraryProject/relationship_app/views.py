from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
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
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'registration/logout.html'

# Check if the user is an Admin
def is_admin(user):
    return user.profile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.profile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.profile.role == 'Member'

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Example: Accessing the profile in a view
def my_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        profile = user.profile
    else:
        # Handle the case where the profile does not exist
        profile = None
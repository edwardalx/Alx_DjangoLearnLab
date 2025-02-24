from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

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

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for logout.
        """
        logout(request)  # Log the user out
        return redirect('home')  # Redirect to the homepage after logout

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests by rendering the logout confirmation page.
        """
def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'


# Example: Accessing the profile in a view
def my_view(request):
    user = request.user
    if hasattr(user, 'profile'):
        profile = user.profile
    else:
        # Handle the case where the profile does not exist
        profile = None
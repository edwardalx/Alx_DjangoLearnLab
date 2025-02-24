from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
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
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log the user in after registration
#             return redirect('home')  # Redirect to the home page
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

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
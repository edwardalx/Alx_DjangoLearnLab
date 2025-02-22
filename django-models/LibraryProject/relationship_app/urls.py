from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
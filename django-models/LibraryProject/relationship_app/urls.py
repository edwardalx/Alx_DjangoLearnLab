from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView
from . import views
from .views import LogoutView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     # Built-in authentication views
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),

    # Custom registration view
    path('register/', views.register, name='register'),
    path('admin/', views.user_is_admin, name='admin_view'),
    path('librarian/', views.user_is_librarian, name='librarian_view'),
    path('member/', views.user_is_member, name='member_view'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
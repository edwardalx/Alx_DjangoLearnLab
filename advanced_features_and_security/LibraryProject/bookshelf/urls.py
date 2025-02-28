from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('edit/', views.edit_book, name='edit_book'),
    path('delete/', views.delete_book, name='delete_book'),
    path('view/', views.book_list, name='view_book'),
    path('form/', views.example_form_view, name='form_view'),
    path('mylist/', views.list_book, name='view_my_list'),
]

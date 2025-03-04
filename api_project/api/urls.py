from django.urls import path
from .views import BookList
urlpatterns = [
path('book/', view=BookList.as_view(), name='book-list'),
]
from django.urls import path
from .views import ListView,DetailView,CreateView,UpdateView,DeleteView,CustomUpdateView,CustomCreateView
urlpatterns = [
    # path('books/', view=ListView.as_view(), name='list-books' ),
    # path('book/<int:pk>/', view=DetailView.as_view(), name='retrieve-book' ),
    # path('book/create', view=CreateView.as_view(), name='create-books' ),
    # path('book/update/<int:pk>/', view=UpdateView.as_view(), name='update-book' ),
    # path('book/delete/<int:pk>/', view=DeleteView.as_view(), name='delete-book' ),
    path('books/', view=ListView.as_view(), name='list-books' ),
    path('book/<int:pk>/', view=DetailView.as_view(), name='retrieve-book' ),
    path('books/create', view=CreateView.as_view(), name='create-books' ),
    path('books/update', view=UpdateView.as_view(), name='update-book' ),
    path('books/delete', view=DeleteView.as_view(), name='delete-book' ),
    path('book/update/<int:pk>/', view=CustomUpdateView.as_view(), name='update-book'),
    path('books/create', view=CustomCreateView.as_view(), name='create-books' ),
]
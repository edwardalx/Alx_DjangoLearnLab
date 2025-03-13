from django.urls import path
from .views import ListView,DetailView,CreateView,UpdateView,DeleteView
urlpatterns = [
    path('book/', view=ListView.as_view(), name='list-books' ),
    path('book/<int:pk>/', view=DetailView.as_view(), name='retrieve-book' ),
    path('book/create', view=CreateView.as_view(), name='create-books' ),
    path('book/update/<int:pk>/', view=UpdateView.as_view(), name='update-book' ),
    path('book/delete/<int:pk>/', view=DeleteView.as_view(), name='delete-book' ),
]
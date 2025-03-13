from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.generics  import ListAPIView, CreateAPIView, UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.views.generic.edit import CreateView, UpdateView
from .models import Book
from .serializers import BookSerializer
from .forms import BookForm


# Create your views here.

class ListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class DetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class CustomCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list-books')
    template_name = 'api/register.html'

    def form_valid(self, form):
        messages.success(self.request, "Book created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))

class UpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list-books')
    template_name = 'api/update.html'
    
    #validate same as I have done in CustomCreateView

class DeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer